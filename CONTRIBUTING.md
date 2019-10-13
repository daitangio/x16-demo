
# Contributing to Commander X16 Demo code

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:


How Can I Contribute?
  * [Reporting Bugs](#reporting-bugs)
  * [Pull Requests](#pull-requests)


## Reporting Bugs
Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/).
Before repoting a bug, ensure it is new, and add a short, simple way to reproduce it.

### Demo xyz is notworking on my emualtor.
Because the emulator is growing faster, sometime the last pushed demo code need the last version of the emulator.

If a code does not work (like sprites) download always the LAST version of the emulator before submiting a bug report

## Pull Requests
The easiest way of contributing is forking the repository and submitting a pull request.

Please follow these steps to have your contribution considered by the maintainers:

### For Basic files:
1. contribute with .bas file (not binary)
2. bas file must be in ascii UTF-8 with uppercase letter 
3. If needed renumber them using the renumber tool (see tools directory)
4. if subrotudine, provide at least one usage example
5. Do not forget to add AUTHOR AND LICENSE information in the head of the file via REMs

### For Assembly code:
1. Group your code in one directory per project
2. Include a Makefile per project
3. Include the directory in the main Makefile, adding it to the SUBDIRS variable (first line) 
4. Test it (see HOW TO COMPILE in the README.md)
5. Do not forget to add AUTHOR AND LICENSE information in the head of the file via ';' comments

## Documentation
For documentation download a copy of the [Commander X16 Programmers Reference](https://github.com/commanderx16/x16-docs)
Commander X16 has a BASIC V2 version derivered from the C/64 one. It will grow and offer more commands in the future.

Take a look at [Commandr X16 Roms project](https://github.com/commanderx16/x16-rom) for a short introduction to the Basic and Kernel services.