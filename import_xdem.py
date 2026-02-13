import subprocess
import importlib
import os
import sys
import pip


def setupxdem():
    try:
        from xdemvenv import xdem
        return xdem
    except ImportError:
        venv_folder = os.path.join(os.path.dirname(__file__),"xdemvenv")

        scripts_folder = os.path.join(venv_folder, "Scripts" if os.name == "nt" else "local/bin")
        
        os.environ["PATH"] += os.pathsep + scripts_folder

        if venv_folder not in sys.path:
            sys.path.insert(0, venv_folder)

        try:
            from xdemvenv import xdem
            print("Import xDEM OK")
            return xdem
        except (ImportError, ModuleNotFoundError):
            print("xDEM not fount, trying to install it")
            os.makedirs(venv_folder, exist_ok=True)

            python_executable = os.path.join(sys.prefix, "python.exe") if os.name == "nt" else "python"
            # nt = windows
            if os.name == "nt":

                subprocess.check_call([
                    python_executable,
                    "-m",
                    "pip",
                    "install",
                    "--target",
                    venv_folder,
                    "xdem"
                ])

            else:
                pip.main(["install", "--target", venv_folder, "xdem"])

            importlib.invalidate_caches()
            if "bulldozer" in sys.modules:
                del sys.modules["bulldozer"]
            sys.path.insert(0, venv_folder)

            try:
                from xdemvenv import xdem
                print("Import xDEM OK")
                return xdem
            except (ImportError, ModuleNotFoundError):
                print("Can't import xDEM trying force it")

                spec = importlib.util.spec_from_file_location("xdem",
                                                              os.path.join(venv_folder,
                                                                           "xdem",
                                                                           "__init__.py"))
                foo = importlib.util.module_from_spec(spec)
                sys.modules["xdem"] = foo

                importlib.invalidate_caches()
                spec.loader.exec_module(foo)
                try:
                    import xdem
                    from xdemvenv import xdem
                    print("Import Bulldozer-dtm OK")
                    return xdem
                except ImportError:
                    print("Failed to import xDEM")
                    raise

imprtxdem = setupxdem()