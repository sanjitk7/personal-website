# Adding photography to the site

Status: **parked**. The Photography section and gallery page are switched off until photos are added.
They turn on automatically as soon as image files exist in `images/photography/`.

## Why not embed VSCO?

Checked on 2026-11-15:

- VSCO sends `X-Frame-Options: SAMEORIGIN`, so the gallery can't be shown in an iframe.
- vsco.co and its image server (im.vsco.co) sit behind a Cloudflare bot check, so hotlinked images are unreliable for visitors.
- VSCO has no official embed or oEmbed endpoint.

So the photos have to be hosted on the site itself. The VSCO link stays as "More on VSCO ↗".

## What to provide

| Item | Requirement |
|---|---|
| Count | 8–12 photos. The first 4 (by filename order) appear on the homepage; all appear on the gallery page. |
| Format | JPG, PNG, HEIC or WebP. Originals are fine; they get converted. |
| Size | Any. They get resized to 1600px on the long edge. |
| Orientation | Mixed is fine for the gallery. The homepage strip crops to 4:5 portrait, so put portrait-friendly shots first. |
| Order | Name them `01-…`, `02-…` etc. to control order. |
| Alt text (optional) | A short description per photo, e.g. `01-rainier.jpg: Mount Rainier from Skyline Trail`. Helps accessibility and search. |
| Rights | Only your own photos. EXIF location data is stripped during processing. |

## How to hand them over

Either attach them in the project thread, or put them in a folder on the Mac (for example
`~/personal_projects/site-photos/`), then say "add these photos to the site".

## What happens next (for whoever implements it)

1. Convert each photo to WebP at 1600px on the long edge, quality ~80, stripping EXIF (`cwebp -resize` or Pillow).
   Also produce an 800px version for the homepage strip if file sizes are large.
2. Save them to `images/photography/` using the ordered filenames.
3. Run `python3 mockups/build.py`. The build detects the files and:
   - adds the Photography section (4-photo strip, "View gallery →", "More on VSCO ↗") and its nav link to the homepage,
   - generates the gallery page (`photography.html`) as a masonry grid.
4. Use the alt text, if given, instead of the generic "Photo by Sanjit Kumar".
5. When going live: add `https://sanjitkumar.me/photography.html` to `sitemap.xml`, and keep the page's own
   title, description and canonical tags.
6. Check the homepage and gallery on a 390px-wide viewport for horizontal overflow, then share screenshots.
