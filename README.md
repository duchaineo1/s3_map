# S3_map

A CLI tool to inspect AWS S3 buckets and gather detailed metrics including size, number of files, and estimated cost.

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

You may also receive:
- Stats on objects by storage class (e.g., how many objects per class in each bucket)
- Filtered output that reflects only the selected storage class
