# sekay

Sekai Analyzer.

sekay = (seka)i + xra(y)

## Android package downloads

Run **Android Package Workflow** with an optional `download_url` pointing to an
XAPK file (including its `manifest.json`). The URL takes precedence over
`app_version_code`. Leave it empty to fetch the latest APKPure package, or set
`app_version_code` to fetch a specific APKPure version. Plain APK links are not
accepted by the XAPK conversion pipeline.

The same `download_url` field is supported in the `android-fetch` repository
dispatch payload and by the **Fetch XAPK Package** workflow. Explicit URLs are
processed even when their version is already recorded. To download only the
XAPK, run **Fetch XAPK Package** with `to_apk: false`.
