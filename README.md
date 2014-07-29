sublime_plugins
===============
My Random Sublime Plugins
This repo is just a bucket where I put the sublime plugins that I happen to write.
Feel free to clone and install them.
At your own risk :)

List of Plugins
---

**font_autoresize.py**

I wanted a plugin that adjusted the fonts of the editor.
Now it resizes to:

| Window Width  | Font Size |
| ------------- |:---------:| 
|   300px      | 10px       | 
|   600px      | 13px       | 
|   900px      | 16px       |
| > 900px      | 20px       | 

Unluckly I could not find if Sublime Text gives an `on_resize` or
`on_update` so I hooked the plugin to `on_modified_async`, `on_activated`, 
and to `on_deactivated`.
