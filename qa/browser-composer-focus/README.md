# Browser composer focus QA

Source: `4d9c978c465bf6dd88f489e581139d344e6c323c` on `fix/focus-chat-on-tab-activation`.

Linux, Chromium through Playwright, real Expo app and isolated real Paseo daemon.
The existing mock agent provider supplies deterministic conversations. Headless
Chromium does not actually blur, so the tests supply browser visibility/focus
signals through the browser environment and exercise the real app handlers.
Videos show the focus and typing results; they do not depict a real OS window
switch. Wide touch-browser emulation covers touch autofocus policy, not a
physical device or software keyboard. Native and packaged Electron are untested.

The two browser-return cases fail on unchanged upstream production code.
Seven additional review regressions fail before their corrections. The final
unchanged-source focus file passes all 20 tests. Workspace typechecks, changed
file lint and formatting, and the independent Claude review pass.

Raw command output and recordings are stored beside this file. NixOS browser
library setup is local test infrastructure, not part of the source change.
