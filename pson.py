import json
import sys

VERSION = "1.0.0"


# -------------------
# CREATE (NEW)
# -------------------
def create(filename, data):
    """
    Creates or overwrites a JSON file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"[pson error] Failed to create file: {e}")


# Alias for backward compatibility
make = create


# -------------------
# READ
# -------------------
def read(filename):
    """
    Prints JSON content in a readable format.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict):
            print(", ".join([f"{k} : {v}" for k, v in data.items()]))

        elif isinstance(data, list):
            for i, item in enumerate(data):
                print(f"[{i}] {item}")

        else:
            print(data)

    except FileNotFoundError:
        print("[pson error] File not found")
    except json.JSONDecodeError:
        print("[pson error] Invalid JSON")
    except Exception as e:
        print(f"[pson error] {e}")


# -------------------
# VALUE (FINAL FIXED)
# -------------------
def value(filename, key=None, index=None):
    """
    Usage:
    pson.value(file) → all values
    pson.value(file, key) → value of key
    pson.value(file, key, index) → array item inside key

    Works with:
    - dict JSON
    - array JSON (list of objects)
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # -------------------
        # NO KEY → return all
        # -------------------
        if key is None:
            if isinstance(data, dict):
                return ", ".join([f"{k} : {v}" for k, v in data.items()])
            elif isinstance(data, list):
                return str(data)
            return str(data)

        # -------------------
        # DICT ROOT
        # -------------------
        if isinstance(data, dict):
            if key not in data:
                return "[pson error] Key not found"

            value_data = data[key]

        # -------------------
        # LIST ROOT (SEARCH FIX)
        # -------------------
        elif isinstance(data, list):
            found = None

            for item in data:
                if isinstance(item, dict) and key in item:
                    found = item[key]
                    break

            if found is None:
                return "[pson error] Key not found in array"

            value_data = found

        else:
            return "[pson error] Unsupported JSON type"

        # -------------------
        # ARRAY INDEX ACCESS
        # -------------------
        if index is not None:
            if not isinstance(value_data, list):
                return "[pson error] Value is not an array"

            try:
                i = int(index)
                return value_data[i]
            except:
                return "[pson error] Invalid array index"

        return value_data

    except FileNotFoundError:
        return "[pson error] File not found"
    except json.JSONDecodeError:
        return "[pson error] Invalid JSON"
    except Exception as e:
        return f"[pson error] {e}"


# -------------------
# CLI
# -------------------
def cli():
    args = sys.argv

    if len(args) > 1 and args[1] == "-v":
        print(VERSION)