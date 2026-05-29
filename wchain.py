def solve_wchain(words_list):
    words_by_length = {}
    for i in range(1, 52):
        words_by_length[i] = []
        
    for word in words_list:
        length = 0
        for char in word:
            length += 1
        
        already_exists = False
        for existing_word in words_by_length[length]:
            if existing_word == word:
                already_exists = True
                break
                
        if not already_exists and length > 0:
            words_by_length[length].append(word)
    
    dp = {}
    max_total_chain = 0
    
    for length in range(1, 52):
        for word in words_by_length[length]:
            max_chain_for_word = 1
            word_len = length
            
            for i in range(word_len):
                subword = ""
                for j in range(word_len):
                    if j != i:
                        subword += word[j]
                
                if subword in dp:
                    current_chain = dp[subword] + 1
                    if current_chain > max_chain_for_word:
                        max_chain_for_word = current_chain
            
            dp[word] = max_chain_for_word
            
            if max_chain_for_word > max_total_chain:
                max_total_chain = max_chain_for_word
                
    return max_total_chain


def main():

    f_in = open("wchain.in", "r")
    lines = f_in.readlines()
    f_in.close()
    
    words_list = []
    is_first = True
    
    for line in lines:
        if is_first:
            is_first = False
            continue
        
        clean_word = ""
        for char in line:
            if char != "\n" and char != "\r" and char != " " and char != "\t":
                clean_word += char
        
        if clean_word != "":
            words_list.append(clean_word)
            
    result = solve_wchain(words_list)
    
    print(result)
    
    f_out = open("wchain.out", "w")
    f_out.write(str(result) + "\n")
    f_out.close()


if __name__ == "__main__":
    main()