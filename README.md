# grpc_py

- The prebuilt files already contain fixed imports

## Requirements

- Python 3.x
- grpcio-tools (install via `pip install grpcio-tools`)

## Usage

### 1. Generating gRPC Files

Before running the Python scripts that utilize gRPC, you might want to regenerate the gRPC Python files from the `.proto` files. Follow the steps below:

#### For Windows:

Run the following command in the root directory of the repository:

```shell
generate_grpc_files.bat
```

- This command will generate the gRPC Python files inside the respective subfolders (account, miiverse, api, friends) within the grpc_py directory.

#### For Unix/Linux:

Run the following command in the root directory of the repository:

```shell
./generate_grpc_files.sh
```

- This command will generate the gRPC Python files inside the respective subfolders (account, miiverse, api, friends) within the grpc_py directory.

### 2. Fixing Imports

To fix the relative import paths in the generated gRPC Python files, you can use the provided Python script named **``fix_imports.py``**. Run the script using the following command:

```shell
python fix_imports.py
```

This script will update the import statements in the generated files to use relative import paths based on the grpc_py directory.