def word_count(s):
    # Your code here
    cache = {}
    result = s.lower()
    cant_Have = r':,;.-+=/\|[]{}()*^&"'

    for characters in result:
        if characters in cant_Have:
            result = result.replace(characters,"")
    words = result.split()
    for word in words:
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))