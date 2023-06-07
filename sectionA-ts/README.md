# Caesar Cipher

This is a TypeScript implementation of the Caesar Cipher algorithm. The Caesar Cipher is a simple substitution cipher that replaces each letter in the plaintext with a letter some fixed number of positions down the alphabet.

## Usage

To use the Caesar Cipher, follow these steps:

1. Ensure you have TypeScript installed on your machine.
2. Clone this repository.
3. Navigate to the project directory.
4. Run the following command to compile the TypeScript code:

   ```
   tsc caesar.ts
   ```

5. Execute the compiled JavaScript code using Node.js:

   ```
   node caesar.js
   ```

   The output will be displayed in the console.

## Examples

Here's an example usage of the Caesar Cipher function:

```typescript
import { caesar_cipher } from './caesar_cipher';

console.log(caesar_cipher('GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.', 39));
```

This will print the decoded message: "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."

## License

This project is licensed under the MIT License.