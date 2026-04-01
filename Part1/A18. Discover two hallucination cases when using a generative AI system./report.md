## Math Question
When prompted with the equation 5.9 + x = 5.11, Microsoft Copilot responded that x = 0.21, treating the problem as straightforward decimal arithmetic. While the algebraic method shown is correct for decimal numbers, the answer is mathematically wrong — 5.11 as a decimal is actually less than 5.9, meaning x would be -0.79, not 0.21.
This is a well documented class of AI hallucination where language models fail to recognise that 5.11 as a decimal number is smaller than 5.9, because in everyday language and software versioning contexts (such as Python 3.9 vs 3.11), 11 intuitively comes after 9. If the model does not know what it does not know, it will present wrong answers with the same confidence as correct ones.

<img width="730" height="680" alt="image" src="https://github.com/user-attachments/assets/a4a1a3bc-a264-4ff6-bf57-32e02a39625f" />

## 
