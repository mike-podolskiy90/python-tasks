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
