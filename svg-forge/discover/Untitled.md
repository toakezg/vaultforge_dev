

```svg
<style>
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  .spin {
    transform-origin: center;
    animation: spin 2s linear infinite;
  }
</style>
      
<svg viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg">
  <circle class="spin" cx="400" cy="400" fill="none"
    r="200" stroke-width="50" stroke="#E387FF"
    stroke-dasharray="948 1400"
    stroke-linecap="round" />
</svg>
```

