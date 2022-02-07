import os
import argparse
import horovod.tensorflow as hvd
import tarfile


def horovod_untar(in_file, out_dir):
    hvd.init()
    if hvd.local_rank() == 0:
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)

    #    if not tarfile.is_tarfile(in_file):
    #        raise Exception()
        tar = tarfile.open(in_file).extractall(out_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='untar file only once per node')
    parser.add_argument('infile', type=str, help='input tar file')
    parser.add_argument('outdir', type=str, help='output directory')
    args = parser.parse_args(    )

    horovod_untar(args.infile, args.outdir)
