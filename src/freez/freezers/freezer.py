from ... import utils


class Freezer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__cleanup_paths: list[str] = []

    def freeze(self, entry: str, output: str) -> None:
        pass

    def install(self) -> None:
        utils.logging.log("Installing...")
        launcher_path = utils.general.app_path(self.name + utils.platform.SCRIPT_EXT)

        with open(launcher_path, "w") as file:
            file.write(
                utils.general.app_path(
                    self.name,
                    self.name,
                )
            )
            file.write(" ")
            file.write("${@:1}" if utils.platform.IS_POSIX else "%*")
        utils.logging.log("Installation complete.", color="green")

    def cleanup(self) -> None:
        for path in self.__cleanup_paths:
            utils.general.delete(path)

    def _add_cleanup_path(self, path: str) -> None:
        if not self.__cleanup_paths:
            self.__cleanup_paths = [path]
        else:
            self.__cleanup_paths.append(path)
