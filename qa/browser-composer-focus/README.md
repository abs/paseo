# Browser composer focus QA

Source: `6974ced8058ddad98f6d3544bfa5a9cb75b7ffb1` on `fix/focus-chat-on-tab-activation`.

Linux, Chromium through Playwright, real Expo app and isolated real Paseo daemon.
The existing mock agent provider supplies deterministic conversations. Headless
Chromium does not actually blur, so the tests supply browser visibility/focus
signals through the browser environment and exercise the real app handlers.
Videos show the focus and typing results; they do not depict a real OS window
switch. Wide touch-browser emulation covers touch autofocus policy, not a
physical device or software keyboard. Native and packaged Electron are untested.

The two browser-return cases fail on unchanged upstream production code.
Six additional review regressions fail before their corrections. The final
unchanged-source focus file passes all 19 tests. Workspace typechecks, changed
file lint and formatting, and the independent Claude review pass.

Raw command output and recordings are stored beside this file. NixOS browser
library setup is local test infrastructure, not part of the source change.
