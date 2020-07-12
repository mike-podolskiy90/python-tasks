## Codesignal tasks: Regular expressions


1. [Check the sentence is correct](is-sentence-correct.py)

    **Task**
    
    Check the sentence is correct. Sentence is considered correct if:
   
   - it starts with a capital letter;
   - it ends with a full stop, question mark or exclamation point ('.', '?' or '!');
   - full stops, question marks and exclamation points don't appear anywhere else in the sentence.
   
   Given a `sentence`, return `true` if it is correct and `false` otherwise.
   
   **Example**
   
   - For `sentence = "This is an example of *correct* sentence."`,
   the output should be
   `is_sentence_correct(sentence) = true`;
   
   - For `sentence = "!this sentence is TOTALLY incorrecT"`,
   the output should be
   `is_sentence_correct(sentence) = false`.
   
   **Input/Output**
   
   - Input: string `sentence`
   
        A string sentence without newline characters
        
   - Output: boolean
   
        `true` if the given `sentence` is correct, `false` otherwise.
   
2. [Swap adjacent words](swap-adjacent-words.py)

    **Task**
    
    You are given a string consisting of words separated by whitespace characters, where the words consist only of English letters. 
    Your task is to swap pairs of consecutive words and return the result.
    
    **Example**
    
    - For `s = "CodeFight On"`, the output should be
    `swap_adjacent_words(s) = "On CodeFight"`;
    - For s = "How are you today guys", the output should be
    `swap_adjacent_words(s) = "are How today you guys"`.
    
    **Input/Output**
    
    - Input: string `s`
    
        A string consisting of whitespace characters (`' '`) and English letters. 
        There is exactly one whitespace character between two consecutive words, and both the first and the last characters of `s` are not equal to `' '`.
    
    - Output: string
    
        String `s` with pairs of adjacent words swapped.
        
3. [N-th number](n-th-number.py)

    **Task**
    
    You are given a string `s` of characters that contains at least `n` numbers (here, a number is defined as a consecutive series of digits, where any character immediately to the left and right of the series are not digits). 
    The numbers may contain leading zeros, but it is guaranteed that each number has at least one non-zero digit in it.
    
    Your task is to find the `n` th number and return it as a string without leading zeros.
    
    **Example**
    
    For `s = "8one 003number 201numbers li-000233le number444"` and `n = 4`,
    the output should be
    `nth_number(s, n) = "233"`.
    
    **Input/Output**
    
    - Input: string `s`
    
    A string containing at least `n` numbers.
    
    - Input: integer `n`
    
    1-based index of the number to find.
    
    - Output: string
    
    The `n` th number without leading zeros.
    
4. [Repetition encryption](repetition-encryption.py)

    **Task**
    
    Jane just got a `letter` from her friend and realized that something's wrong: some words in the `letter` are written twice in a row. The thing is, she and her friend devised an ingenious cypher, the key to which is the number of pairs of repeated words in the encoded text. The cases of the words don't matter.
    
    Formally, a word is a substring of `letter` consisting of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not letters.
    
    For obvious reasons, Jane can't tell you how the encryption works, but she needs your help with calculating the number of pairs of consecutive equal words. Write a function that, given a `letter`, returns this number.
    
    **Example**
    
    For `letter = "Hi, hi Jane! I'm so. So glad to to finally be able to write - WRITE!! - to you!"`,
    the output should be
    `repetition_encryption(letter) = 4`.
    
    There are `4` pairs of consecutive identical words in the text. They are shown below:
    "**Hi, hi** Jane! I'm **so. So** glad **to to** finally be able to **write - WRITE**!! - to you!"
    
    **Input/Output**
    
    - Input: string `letter`
    
    The letter Jane's friend wrote to her. 
    It is guaranteed that there are no more than two consecutive equal words in a row. 
    It is also guaranteed that between two such pairs there are at least two symbols.
    
    - Output: integer
    
    The number of pairs of consecutive equal words in the `letter`.
