from rtlsdr import RtlSdr


def main():
    # Use a context manager to ensure device is closed cleanly
    with RtlSdr() as sdr:
        # Configure basic parameters
        sdr.sample_rate = 2.4e6    # Hz
        sdr.center_freq = 100e6    # Hz (e.g. 100 MHz)
        sdr.gain = 'auto'          # or set numeric value like 40

        print("RTL-SDR instantiated with:")
        print(f"  sample_rate = {sdr.sample_rate}")
        print(f"  center_freq = {sdr.center_freq}")
        print(f"  gain = {sdr.gain}")

        # Read a block of samples
        samples = sdr.read_samples(256 * 1024)
        print(f"Read {len(samples)} complex samples")

if __name__ == "__main__":
    main()