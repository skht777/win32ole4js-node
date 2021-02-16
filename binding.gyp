{
  "variables": {
    "module_name%": "win32ole4js",
    "module_path%": "lib"
  },
  'targets': [
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    },
    {
      'target_name': 'win32ole4js',
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'sources': [
	    # TBD
      ]
    }
  ]
}