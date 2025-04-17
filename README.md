# S3_map

A CLI tool to inspect AWS S3 buckets and gather detailed metrics including size, number of files, and estimated cost.

## Installation

```bash
pip install s3-map
```

## Usage

```bash
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-west-2
PACKAGE_LOCATION=$(pip show s3-map | grep Location | awk '{print $2}')
cd "$PACKAGE_LOCATION/s3_map"
python3 ./main.py --help
```

## CLI Arguments

| Short | Long           | Description                                                                                       | Type   | Choices                                        | Default |
|-------|----------------|---------------------------------------------------------------------------------------------------|--------|------------------------------------------------|---------|
| `-b`  | `--bucket`     | Name of the bucket to fetch                                                                       | `str`  | –                                              | –       |
| `-r`  | `--region`     | display buckets grouped by region                      | `switch`  | –                                              | –       |
| `-u`  | `--unit`       | Unit to return bucket size in                                                                     | `str`  | `b`, `kb`, `mb`, `gb`, `tb`                    | `b`     |
| `-s`  | `--storageclass` | Process only objects of a specific storage class. Defaults to `None`                            | `str`  | `STANDARD`, `STANDARD_IA`, `REDUCED_REDUNDANCY` | `None`  |
## Output Information

For each bucket, the tool returns the following information:

- **Name**
- **Creation date**
- **Number of files**
- **Total size of files**
- **Last modified date of the most recent file**
- **Estimated storage cost**
- **region**

## Supported Options

### Display Options

- Display bucket sizes in different units:
  - `b`, `kb`, `mb`, `gb`, `tb`
- Group buckets by region

### Filter Options

- Filter by bucket name
- Filter by storage class:
  - `STANDARD`
  - `STANDARD_IA`
  - `REDUCED_REDUNDANCY`
