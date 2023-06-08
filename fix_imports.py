import os
import re


def replace_grpc_imports(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                with open(file_path, "r") as file:
                    content = file.read()
                modified_content = re.sub(r"^(import.*pb2)", r"from . \1", content, flags=re.MULTILINE)
                with open(file_path, "w") as file:
                    file.write(modified_content)


replace_grpc_imports("./account")
replace_grpc_imports("./api")
replace_grpc_imports("./miiverse")
replace_grpc_imports("./friends")
