### v2.2.1
- Changed version checking to use official GitHub API
- As language file is the one to be created it now also serves as a folder write check

### v2.2
- Made the part that gets rid of empty rows more logical
- Got rid of retries, now if an error occurs while trying to reach any website the app doesn't try again, thus saving the website's bandwitch
- Added a short license splash screen, reminding users that the program comes without any warranty

### v2.1.2
- Fixed Main window pages breaking the Edit window

### v2.1.1
- Fixed book details staying in the Add window even after the book has been added successfully

### v2.1

**Improvements:**

- Total app rework
  - GUI reworked - now features tabs, instead of confusing window system
  - Languages reworked - instead of two different editions you now have one with a pop-up at first launch, asking you which language you'd like to use
- Number padding function has been added, so when you sort by ID it always sorts the right way
- Quality of live improvement, some buttons (mostly OK(-esque) ones) now have the return (/Enter) key bound to them
- Add window now shows the ID of the added book
- Main window now uses pages, so even bigger parrotex-es shouldn't have an issue showing on older computers
- You can now launch the Edit window from Search
- Instead of disappearing while processing your request (e.g. ISBN data load), a loading window appears

**Fixes:**

- ISBN errors fixed - no internet connection and valid, yet empty ISBN
- Window size is now smaller and shouldn't overflow
- Fixed the ID change (again), now it should only change when you change location's first letter, which is the one that makes the ID
- Added an error that pops up if you launch the software in a protected/system folder

### v2.0

- Fixed the program crashing when no internet connection was available (see Issue [#1](https://github.com/FTEdianiaK/library-parrotex/issues/1))
- Fixed the ID being changed by every edit, not only when the location changes
- CS: Translated file names into Czech as to avoid conflicts with the English version (see Issue [#2](https://github.com/FTEdianiaK/library-parrotex/issues/2))
- CS: Fixed a slight error in translation from English
- CS: Translated docstrings into Czech
- CS: Fixed confirmation windows not closing

### v1.1

- Added location retention for the add window - No more having to rewrite the location every time while working on the same shelf/section
- Reworked the search parameters to be case-insensitive
- Added a splash screen that shows the software's current version
- Added a function that checks for updates upon launch
- Confirmation windows have been changed to better fit their questions
- CS: Confirmation windows have been translated into Czech

### v1.0

- First stable version