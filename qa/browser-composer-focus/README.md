# Browser composer focus QA

Source: `a3dd4beebec5d66e46cc4aa12c7d6092e3bce714` on `fix/focus-chat-on-tab-activation`.

Linux, Chromium through Playwright, real Expo app and isolated real Paseo daemon.
The existing mock agent provider supplies deterministic conversations. Headless
Chromium does not actually blur, so the tests supply browser visibility/focus
signals through the browser environment and exercise the real app handlers.
Videos show the focus and typing results; they do not depict a real OS window
switch. Wide touch-browser emulation covers touch autofocus policy, not a
physical device or software keyboard. Native and packaged Electron are untested.

The two browser-return cases fail on unchanged upstream production code.
Five additional review regressions fail before their corrections. The final
unchanged-source focus file passes all 18 tests. Workspace typechecks, changed
file lint and formatting, and the independent Claude review pass.

Raw command output and recordings are stored beside this file. NixOS browser
library setup is local test infrastructure, not part of the source change.
