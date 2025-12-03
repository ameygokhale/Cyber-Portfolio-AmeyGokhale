# CyberChef

This repository contains reusable [CyberChef](https://gchq.github.io/CyberChef/) recipes in JSON format.

CyberChef is a web-based "Cyber Swiss Army Knife" for encoding/decoding, data analysis, and transformation. Recipes can be saved and shared as JSON and then pasted back into CyberChef to re-use. 

## How to use these recipes

1. Open CyberChef in your browser.
2. Click on the **"Recipe"** panel menu (the small disk icon) and choose **"Load recipe"**.
3. Copy the contents of a `.json` file from the `recipes` folder in this repo.
4. Paste it into the "Recipe" box in CyberChef's *Load recipe* dialog.
5. Click **Load** – the operations will appear in the Recipe column.
6. Paste or load your input data and click **Bake!**.

## Included recipes

### 1. decode_web_payload.json

**Use case:**  
Common pattern in malware / web debugging: data is URL-encoded, then Base64-encoded, then GZIP-compressed.  
This recipe does:

1. `URL Decode`
2. `From Base64`
3. `Gunzip`

So if you have a suspicious string like:

- URL encoded → Base64 blob → GZIP data

you can quickly decode it back to its original text or script.

## Adding your own recipes

1. Build a recipe in CyberChef (drag operations into the Recipe panel).
2. Click the **Save** icon in the Recipe panel.
3. Choose **“Clean JSON”** or **“Compact JSON”** format.
4. Copy the JSON and save it as a new file under the `recipes/` folder, e.g. `my_new_recipe.json`.
5. Commit and push to GitHub.

## License

Feel free to change this, but by default:

MIT License – do whatever you want, just keep a copy of the license.
