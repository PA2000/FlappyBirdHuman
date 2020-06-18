import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
   name="FlappyBird",
   options={"build_exe": {"packages": ["pygame"], "include_files": ["Base.py", "Bird.py", "Pipe.py", "imgs"]}},
   executables = executables
)
