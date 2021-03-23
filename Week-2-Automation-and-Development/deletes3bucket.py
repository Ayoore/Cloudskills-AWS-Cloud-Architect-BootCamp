import sys
import boto3

try:
    def main():
        delete_s3bucket(bucket_name)

except Exception as e:
    print(e)


def delete_s3bucket(bucket_name):
    s3_bucket = boto3.client(
        's3',
    )

    delete = s3_bucket.delete_bucket(
        Bucket=bucket_name,
    )

    print(delete)


bucket_name = sys.argv[1]

if __name__ == '__main__':
    main()

