## Karabiner bluetooth keyboard shortcut
```json
{
    "title": "Bluetooth Connect",
    "rules": [
        {
            "description": "Connect to AirPods",
            "manipulators": [
                {
                    "from": {
                        "key_code": "a",
                        "modifiers": {
                            "mandatory": ["fn"]
                        }
                    },
                    "to": [
                        {
                            "shell_command": "/usr/local/bin/blueutil -p 1; /usr/local/bin/blueutil --connect \"AirPods Pro\""
                        }
                    ],
                    "type": "basic"
                }
            ]
        }
    ]
}
```