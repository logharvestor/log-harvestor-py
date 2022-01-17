<p align="center"><a href="https://www.logharvestor.com" target="_blank" rel="noopener" referrerpolicy='origin'><img width="70%" src="https://i.ibb.co/gwFL3jk/logo-drk.png" alt="LogHarvestor Logo"></a></p>


<p align="center">
  <a href="https://www.linkedin.com/company/log-harvestor" rel="nofollow">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="Log Harvestor - LinkedIn"> 
  </a> &nbsp; 
  <a href="https://twitter.com/LogHarvestor" rel="nofollow">
    <img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white" alt="LogHarvestor - Twitter">
  </a> &nbsp; 
  <a href="https://www.youtube.com/channel/UCS9BdZPla9UbUQ3AZJEzVvw" rel="nofollow">
    <img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="Log Harvestor - You Tube">
  </a>
</p>

# log-harvestor-py

## Documentation
See [API Docs](https://www.logharvestor.com/docs/api) for Log-Harvestor API Documetnation.

This package is specific to `Python`. 

Please see our [docs](https://www.logharvestor.com/docs) for other supported languages, or use standard HTTP requests.

## Installation
______________

```console
pip install log-harvestor-py
```

## Usage
_____________
This package requires that you have a **Log Harvestor** account, and *Forwarder's* created.
If you have not done this yet:
1. Go to [LogHarvestor.com](https://www.logharvestor.com)
2. Register for a new Account (This is free) [Register](https://app.logharvestor.com/register)  
3. Create a new Forwarder - [Link](https://app.logharvestor.com/forwarder)
4. Generate a Forwarder Token

Now you can use this forwarder token to send logs, by adding it to the config:
```Python
  from logharvestor import Forwarder

  pvt_token  = 'your_forwarder_token'
  fwdr = Forwarder(token=token, verbose=True)
  fwdr.log('test', {"title": 'Hello World'})
```
## Configuration
___________

| Option      | Default                          | Description                                   |
| :---------- | :------------------------------- | :-------------------------------------------- |
| **Token**   | ""                               | The JWT token assigned to your forwarder      |
| **ApiUrl**  | https://app.logharvestor.com/log | This should never change unless using proxies |
| **Verbose** | false                            | Verbose mode prints info to the console       |


## Examples
- ### **Configuring**
```Python
  from logharvestor import Forwarder

  pvt_token := "your_forwarder_token"
  fwdr = Forwarder(token=token, verbose=True)
```
- ### **Test Connection**
```Python
  from logharvestor import Forwarder

  pvt_token := "your_forwarder_token"
  fwdr = Forwarder(token=token, verbose=True)
  
  success, res = fwdr.test_conn()
  # `success` != True, the connection failed
  # `res` contains the error that occured

  # Error Examle (Invalid Token):
  #   False, <Response [401]> 
  
```

- ### **Logging**
```Python
  from logharvestor import Forwarder

  pvt_token := "your_forwarder_token"
  fwdr = Forwarder(token=token, verbose=True)

  # Strings
  fwdr.log('test', msg="Hello World!")

  # Numbers
  fwdr.log('test', msg=123)

  # Objects / Dicts
  fwdr.log('test', msg={"a": 123, "b": "456", "c": "hello"})

  # Arrays / Lists
  fwdr.log('test', msg=["hello", "mars", "goodbye", "world"]))
  fwdr.log('test', msg=[1, 2, 34, 567, 8, 90])

  # Mixed
  fwdr.log('test', msg={"a": 123, "b": {"c": "123", "d": {}}})

  # Nested
  fwdr.log('test', msg=[123, "abc", [1, 2, 3], {"question": "Hello?", "answer": "World!"}, {"question": "So long?", "answer": "Thanks for all the fish!"}])

```

## Recomendations
________________
1. Keep your Logging specific, and consise. This makes searching faster and more accurate
2. No need to add timestamps or info about the forwarder. This information is automatically included with the log.



<p align="center"><a href="https://www.logharvestor.com" target="_blank" rel="noopener" referrerpolicy='origin'><img width="100" src="https://i.ibb.co/80sThNP/icon-drk.png" alt="LogHarvestor Logo"></a></p>
