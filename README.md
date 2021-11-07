
# API d'insultes françaises

Une API simple avec plus de 100 insultes françaises. 


## Exemple d'utilisation

```python
import requests

response=requests.get('http://insultefr.mywire.org/api')
print(response.json())
```

## API Reference

#### Insulte aléatoire

```http
  GET /api
```


#### Toutes les insultes

```http
  GET /api/all
```


## Contributions

Les contribution sont toujours les bienvenues!

N'hésitez pas à améliorer le code ou à ajouter de nouvelles insultes



## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

