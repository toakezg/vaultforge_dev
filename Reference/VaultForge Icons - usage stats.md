# VaultForge Icons - Usage Stats

## Purpose

Track cost, output volume, client value, and repeatability for icon/logo jobs.

## First CSV Shape

```csv
date,client,job,profile,preset,style,quantity,generated,selected,delivered,prompt_text_tokens,input_image_tokens,output_image_tokens,estimated_cost,price_charged,time_minutes,ad_source,lead_status,notes
```

## Track Per

- icon
- bundle
- pack
- preset
- style
- profile
- client

## Cost Notes

OpenAI image generation cost is tied to image size, quality, and generated image tokens.

If image editing is added later, input image tokens should be tracked separately from output image tokens.

Reference:

- https://developers.openai.com/api/docs/guides/image-generation
