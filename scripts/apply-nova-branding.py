#!/usr/bin/env python3
"""Apply the small, versioned NovaLauncher branding patch to the pinned upstream source."""
from pathlib import Path

source = Path("upstream/ZalithLauncher2/ZalithLauncher/src/main/java/com/movtery/zalithlauncher/ui/activities/MainActivity.kt")
text = source.read_text(encoding="utf-8")

marker = "/* NOVALAUNCHER_UNOFFICIAL_NOTICE */"
if marker in text:
    print("NovaLauncher notice patch already applied.")
    raise SystemExit(0)

anchor = "                ObserveFullScreenSetting(AllSettings.launcherFullScreen.state)" + chr(10)
if text.count(anchor) != 1:
    raise SystemExit("Expected exactly one main-screen insertion point; refusing to patch unknown upstream source.")

imports_anchor = "import androidx.activity.compose.setContent" + chr(10)
imports = [
    "import androidx.compose.material3.AlertDialog",
    "import androidx.compose.material3.Text",
    "import androidx.compose.material3.TextButton",
    "import androidx.compose.runtime.mutableStateOf",
    "import androidx.compose.runtime.remember",
    "import androidx.compose.runtime.setValue",
]
if text.count(imports_anchor) != 1:
    raise SystemExit("Could not locate Compose imports safely.")
missing_imports = [item for item in imports if item not in text]
text = text.replace(imports_anchor, imports_anchor + chr(10).join(missing_imports) + chr(10), 1)

notice = '''                // NOVALAUNCHER_UNOFFICIAL_NOTICE
                var showUnofficialNotice by remember { mutableStateOf(true) }
                if (showUnofficialNotice) {
                    AlertDialog(
                        onDismissRequest = { showUnofficialNotice = false },
                        title = { Text("NovaLauncher") },
                        text = {
                            Text(
                                "Unofficial Modified Version. NovaLauncher is an independent " +
                                    "community modification and is not an official upstream release."
                            )
                        },
                        confirmButton = {
                            TextButton(onClick = { showUnofficialNotice = false }) {
                                Text("Continue")
                            }
                        }
                    )
                }

'''
text = text.replace(anchor, anchor + notice, 1)
source.write_text(text, encoding="utf-8")
print(f"Applied NovaLauncher startup notice to {source}.")
