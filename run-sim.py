import argpars





















def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c" help="configuration YAML")
    parser.add_argument("--debug", action="store_true", help="print additional debug info")
