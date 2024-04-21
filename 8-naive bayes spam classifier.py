#Classify text message as spam or not spam using Naive Bayes classifier. 

# Sample data - spam and ham messages 

spam_messages = [ 

    "WINNER! You've won a free vacation. Claim now!", 

    "Buy cheap viagra, cialis, and more.", 

    "Congratulations! You've been selected to receive $1000 cash prize." 

] 

  

ham_messages = [ 

    "Hey, what's up?", 

    "Can you pick up some groceries on your way home?", 

    "Reminder: Meeting at 3 PM." 

] 

  

# Split messages into words 

spam_words = [word.lower() for message in spam_messages for word in message.split()] 

ham_words = [word.lower() for message in ham_messages for word in message.split()] 

  

# Calculate word frequencies 

spam_word_freq = {word: spam_words.count(word) for word in set(spam_words)} 

ham_word_freq = {word: ham_words.count(word) for word in set(ham_words)} 

  

# Total number of words 

total_spam_words = sum(spam_word_freq.values()) 

total_ham_words = sum(ham_word_freq.values()) 

  

# Test messages 

test_messages = [ 

    "Congratulations! You're the lucky winner.", 

    "Hey, are you free for lunch today?" 

] 

  

# Classify test messages 

for message in test_messages: 

    message_words = message.lower().split() 

    spam_probability = 1.0 

    ham_probability = 1.0 

    for word in message_words: 

        spam_probability *= (spam_word_freq.get(word, 0) + 1) / (total_spam_words + len(set(spam_words))) 

        ham_probability *= (ham_word_freq.get(word, 0) + 1) / (total_ham_words + len(set(ham_words))) 

    if spam_probability > ham_probability: 

        print("SPAM") 

    else: 

        print("NOT SPAM") 


"""  NOT SPAM
NOT SPAM


** Process exited - Return Code: 0 **
Press Enter to exit terminal  """"
