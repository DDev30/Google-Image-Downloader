import os
import argparse

def run_pipeline(keyword, max_num, Down_storage_dir,  recipient_email):
    os.system(f"python download.py {keyword} \"{max_num}\" \"{Down_storage_dir}\"")
    os.system(f"python zip.py \"{Down_storage_dir}\" \"{Down_storage_dir}.zip\"")
    os.system(f"python sendToEmail.py \"{Down_storage_dir}.zip\" \"{recipient_email}\"")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword")
    parser.add_argument("max_num", type=int)
    parser.add_argument("downstorage_dir")
    parser.add_argument("recipient_email")

    args = parser.parse_args()
    run_pipeline(args.keyword, args.max_num, args.downstorage_dir, args.recipient_email)
