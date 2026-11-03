# Asset provenance

- `app-icon.png`: 512×512 derivative of the owner's official 1024×1024 Clipzelo app icon, supplied by the local iOS app's `AppIcon.appiconset/AppIcon.png`. Resized with Pillow's Lanczos filter; artwork is unchanged.
- `apple-touch-icon.png`: 180×180 derivative of the same official icon.
- `favicon.png`: 32×32 derivative of the same official icon.
- `app-store-qr.png`: locally generated, black on white, 360×360 QR code, error correction M, with a four-module quiet zone. Created with Python `qrcode` 8.2. Payload:

```text
https://apps.apple.com/us/app/clipzelo-video-compressor/id6824147929
```

The QR image was independently decoded with Apple's Vision barcode reader before review. These tools are authoring/verification tools only; visitors load no external QR service or scripts. No screenshots or simulated product UI are used.
