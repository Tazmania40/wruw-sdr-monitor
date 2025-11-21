from rtlsdr import RtlSdr
import numpy as np
import scipy.signal as signal
import sounddevice as sd
from scipy.signal import resample_poly, firwin, bilinear, lfilter

SDR_SAMPLE_RATE = 2.4e6  # SDR sample rate (e.g., 2.4 MS/s)
CENTER_FREQ = 91.1e6      # Center frequenc (e.g., 100 MHz FM band)
AUDIO_SAMPLE_RATE = 44000 # Standard audio sample rate (e.g., 44.1 kHz)
DURATION = 5             # Duration to record (seconds)

def main():
    sdr = RtlSdr()

    sdr.sample_rate = SDR_SAMPLE_RATE
    sdr.center_freq = CENTER_FREQ
    sdr.gain = 'auto'         

    # Read a block of samples
    x = sdr.read_samples(SDR_SAMPLE_RATE * DURATION)

    # Demodulation
    x = np.diff(np.unwrap(np.angle(x)))

    # De-emphasis filter, H(s) = 1/(RC*s + 1), implemented as IIR via bilinear transform
    bz, az = bilinear(1, [75e-6, 1], fs=SDR_SAMPLE_RATE)
    x = lfilter(bz, az, x)

    # decimate by 6 to get mono audio
    x = x[::54]
    sample_rate_audio = SDR_SAMPLE_RATE/54

    # normalize volume so its between -1 and +1
    x /= np.max(np.abs(x))
    
    audio_signal = x
    resampled_audio = audio_signal.astype(np.float32)


    print(f"Playing audio at {sample_rate_audio} Hz...")
    # Play the numpy array
    sd.play(resampled_audio, samplerate=sample_rate_audio)
    sd.wait() # Wait until the audio is finished playing
    print("Playback finished.")


# Function to perform FM demodulation (simplified)
def fm_demodulate(iq_data):
    return 0.5 * np.angle(iq_data[0:-1] * np.conj(iq_data[1:]))


if __name__ == "__main__":
    main()