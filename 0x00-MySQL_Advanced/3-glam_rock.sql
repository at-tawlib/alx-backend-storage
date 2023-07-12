-- lists all bands with Glam rock as their main style ranked by longevity
SELECT band_name,
    (IFNULL(split, 2022) - formed) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam Rock%'
ORDER BY lifespan DESC
