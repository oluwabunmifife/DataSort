# DataSort
Taking json payload and sorting it in a way that is useful for the user 👨🏾‍💻👩🏾‍💻  <br><br>

## Approach One

- Open the json file
- ```json.load``` the file; This will return a dictionary. <br> NB: NOT ```json.loads```
  
- In my case, I was only interested in the ```Statement``` 'Key' <br> So I 'zeroed' in on what I needed.
- Then I looped through with the Condition I wanted to check for; ```if y["DebitCredit"] == "C"```

<br><br><br>

## Approach Two -> Mapper Implementation (This one was more fun 🤓)
- Open the json file ```open``` function
- ```json.load``` the file; <br> Again, NOT ```json.loads```
- Use the ```map``` function while turning it to a list ```result = list(map(checker, i))``` <br> Where ```checker``` is the function that houses the condition used by the
```map``` function
- Then finanlly looping through the result to return it as a dictionary😏
