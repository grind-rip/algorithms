"""
Manacher's Algorithm
--------------------

Manacher's Algorithm was discovered by Glenn K. Manacher in 1975 and can be
used to find the longest palindromic substring of a string and all palindromic
substrings of a string in linear time.

Definitions
-----------
A palindrome is a sequence that reads the same forward as backward. So, given a
string `s`, a substring of `s` of length n is a palindrome if s[i] = s[n-i] for
all 0 ≤ i ≤ n-1.

A brute force approach
----------------------
The total number of substrings in a string of length n is n(n + 1)/2. Checking
each substring is a O(n). So, a naive solution that enumerates all substrings
and checks their palindromicity has O(n^3) time complexity.

Subalgorithms
-------------
Manacher's Algorithm leverages the following subalgorithms in its
implementation:
 1. Expansion around centers
 2. Augmentation with separator
 3. Palindromic radii array

Since each subalgorithm introduces an order of complexity, they are represented
as separate functions below.

Expansion around centers
------------------------
An improvement to the brute force approach involves expansion around each
potential palindrome's center, which brings the time complexity down to O(n^2)
(2*n-1 centers * n/2 comparisons).

Manacher's Algorithm builds from this trivial algorithm that is based on the
fact that a palindrome can be expanded if s[0] and s[n-1] are equal. This
algorithm is slow, however, requiring O(n^2) time complexity.

Augmentation with separator
---------------------------
A strategy for handling both odd and even length palindromes (palindromes
centered around one or two characters, respectively), is to use a separator.
For example, the string "noon" becomes "|n|o|o|n|".

Odd length palindrome:

  a c b a b c a
        i
      | - |
    | ----- |
  | --------- |

Even length palindrome:        Even length palindrome (with separator):

  a c b aa b c a                 | a | c | b | a | a | b | c | a |
         i                                       i
      | -- |                                   | - |
    | ------ |                             | --------- |
  | ---------- |                       | ----------------- |
                                   | ------------------------- |

Palindromes of odd and even lengths can be accounted for using two separate
arrays. In the case of even length palindromes, the center is taken as s[i] and
s[i-1]. Using a separator, however, we coerce the original string into an odd
length. In doing so, we then only need to account for odd length palindromes,
which reduces the complexity of the logic.

Palindromic radii array
-----------------------
Instead of storing the length of each palindrome at element i, we store its
radius. The radius measures the distance from the center to the edge of the
palindrome (not including the center itself). The key advantage of storing
radii instead of actual lengths is that it allows for the algorithm's core
optimization: using previously computed palindromes to avoid redundant
character comparisons.

Manacher's Algorithm
--------------------
We observe that palindromes with a common center form a contiguous chain, that
is, if we have a palindrome of length `n` centered at `i`, we also have
palindromes of length n-2, n-4, and so on also centered at `i`. Storing this
information allows us to make assertions about the possible length of other
palindromic substrings in the string. For example, given the string "abacaba",
we observe that the longest palindrome is centered at "c". Since, by
definition, all characters after "c" must be equal to all characters before
"c", characters within the radius of the palindrome centered at "c" must have
at least the same palindromic radius (i.e., the same longest palindrome) as the
characters before "c". Characters before "c" are commonly referred to as
"mirrored" centers.

  a b a c a b a        * Since the characters after "c" are within its
  0 1 0 3 - - -          palindromic radius, they must share the same
        ^                palindromic radii with the characters before "c".
        i

There are special cases to consider, however. The above case represents the
nominal case in which the palindrome for the centers after "c" lie completely
within the palindrome centered at "c". In this case, the palindromes centered
after "c" have the same palindromic radius as their mirrored centers ("b" and
"b", for example).

The second case is when the palindrome for the center extends outside the
original palindrome. That is, it extends beyond its left boundary.

  a b a c a b x        * Since the palindrome for the mirrored center extends
  0 1 0 2 - - -          beyond the left boundary of the original palindrome,
        ^                the palindrome for the center ("b") can only extend
        i                to the boundary of the original palindrome, which in
    | ----- |            this case is 0.
  | - |

The third case is when the palindrome for the mirrored center extends exactly
up to the border of the original palindrome. In this case, it is impossible to
know for sure the palindromic radius of the center–we only know that it is at
least as long as its mirrored center. In this case, we initialize the radius at
the new center to be the mirrored center and attempt to expand the palindrome,
thus removing the redundant checks for characters within the new center's
radius.

  x b a c a b a        * Since the palindrome for the mirrored center extends
  0 0 0 2 - - -          up to the left boundary of the original palindrome,
        ^                the palindrome for the center ("b") is at least as
        i                long as the mirrored center, which is 0; however, the
    | ----- |            actual palindromic radius is 1.
    | - |
"""


def expansion_around_centers(s: str) -> str:
    """
    A slow, O(n^2) algorithm that finds the longest palindromic substring by
    attempting to build a palindrome from each possible center. Odd length and
    even length palindromes are handled separately.
    """
    if not s:
        return ""

    start, end, maximum_length = 0, 0, 0

    # Check for odd length palindromes (centered at each character).
    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > maximum_length:
                maximum_length = current_length
                start, end = left, right
            left -= 1
            right += 1

    # Check for even length palindromes (centered at each character pair).
    for i in range(len(s) - 1):
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > maximum_length:
                maximum_length = current_length
                start, end = left, right
            left -= 1
            right += 1

    return s[start : end + 1]


def augmentation_with_separator(s: str) -> str:
    """
    A slow, O(n^2) algorithm that finds the longest palindromic substring by
    attempting to build a palindrome from each possible center. Odd length and
    even length palindromes are handled jointly by augmenting the original
    string with a separator between each character.
    """
    if not s:
        return ""

    # Preprocess string to handle odd and even length palindromes.
    # For example, the string "noon" becomes "|n|o|o|n|".
    s_prime = "|" + "|".join(s) + "|"

    start, end, maximum_length = 0, 0, 0

    for i in range(len(s_prime)):
        left, right = i, i
        while left >= 0 and right < len(s_prime) and s_prime[left] == s_prime[right]:
            current_length = right - left + 1
            if current_length > maximum_length:
                maximum_length = current_length
                start, end = left, right
            left -= 1
            right += 1

    # Convert back to indices in the original string.
    start, end = start // 2, (end - 1) // 2
    return s[start : end + 1]


def palindromic_radii_array(s: str) -> str:
    """
    A slow, O(n^2) algorithm that finds the longest palindromic substring by
    attempting to build a palindrome from each possible center. Odd length and
    even length palindromes are handled jointly by augmenting the original
    string with a separator between each character. A palindromic radii array
    is built, which stores the distance from the center to the edge of the
    palindrome (not including the center itself).
    """
    # Create S' by inserting a separator character '|' between each character.
    # This allows for the consolidation of the odd and even palindromic arrays
    # into a single array. Odd palindromes are centered around non-separator
    # characters, even palindromes are centered around separator characters.
    s_prime = "|" + "|".join(s) + "|"

    # A palindromic radii array is used to store the radius of the longest
    # palindrome centered on each character in S'. It is important to note that
    # `palindrome_radii` contains the radius of the palindrome, not the length
    # of the palindrome itself.
    palindrome_radii = [0] * len(s_prime)

    center = 0

    while center < len(s_prime):
        # Determine the longest palindrome centered at `center` starting from
        # s_prime[center - radius] and ending at s_prime[center + radius]. This
        # technique expands around a given center, using the assertion that a
        # palindrome can be expanded if the start and end characters of the new
        # substring are equal.
        radius = 0
        while (
            center - (radius + 1) >= 0
            and center + (radius + 1) < len(s_prime)
            and s_prime[center - (radius + 1)] == s_prime[center + (radius + 1)]
        ):
            radius += 1
        # Store the radius of the longest palindrome in the array.
        palindrome_radii[center] = radius
        center += 1

    # The longest palindrome in S is formed from the center with the largest
    # radius.
    max_radius, max_center = 0, 0
    for i in range(len(palindrome_radii)):
        if palindrome_radii[i] > max_radius:
            max_radius, max_center = palindrome_radii[i], i

    # Convert back to indices in the original string.
    start, end = (max_center - max_radius) // 2, (max_center + max_radius - 1) // 2
    return s[start : end + 1]


def manachers_algorithm(s: str) -> str:
    """
    Manacher's Algorithm. Finds the longest palindromic substring of a string
    in linear time.
    """
    # Create S' by inserting a separator character '|' between each character.
    # This allows for the consolidation of the odd and even palindromic arrays
    # into a single array. Odd palindromes are centered around non-separator
    # characters, even palindromes are centered around separator characters.
    s_prime = "|" + "|".join(s) + "|"

    # A palindromic radii array is used to store the radius of the longest
    # palindrome centered on each character in S'. It is important to note that
    # `palindrome_radii` contains the radius of the palindrome, not the length
    # of the palindrome itself.
    palindrome_radii = [0] * len(s_prime)

    # NOTE: In some implementations `right` may be used instead of `radius` to
    # denote the boundary of palindrome centered at `center`.
    center, radius = 0, 0

    while center < len(s_prime):
        # Determine the longest palindrome centered at `center` starting from
        # s_prime[center - radius] and ending at s_prime[center + radius]. This
        # technique expands around a given center, using the assertion that a
        # palindrome can be expanded if the start and end characters of the new
        # substring are equal.
        while (
            center - (radius + 1) >= 0
            and center + (radius + 1) < len(s_prime)
            and s_prime[center - (radius + 1)] == s_prime[center + (radius + 1)]
        ):
            radius += 1
        # Store the radius of the longest palindrome in the array.
        palindrome_radii[center] = radius

        # The following is the algorithm's core optimization.

        # Save the center and radius of the original palindrome.
        original_center, original_radius = center, radius
        center, radius = center + 1, 0

        while center <= original_center + original_radius:
            # Calculate the "mirrored" center for the current center.
            mirrored_center = original_center - (center - original_center)
            # Calculate the maximum possible radius of the palindrome centered
            # at `center`.
            max_radius = original_center + original_radius - center

            # Case 1: Palindrome of mirrored center lies entirely within the
            # original palindrome.
            if palindrome_radii[mirrored_center] < max_radius:
                palindrome_radii[center] = palindrome_radii[mirrored_center]
                center += 1
            # Case 2: Palindrome of mirrored center extends beyond the boundary
            # of the original palindrome.
            elif palindrome_radii[mirrored_center] > max_radius:
                palindrome_radii[center] = max_radius
                center += 1
            # Case 3: Palindrome of mirrored center extends exactly up to the
            # boundary of the original palindrome.
            else:
                radius = max_radius
                break

    # The longest palindrome in S is formed from the center with the largest
    # radius.
    max_radius, max_center = 0, 0
    for i in range(len(palindrome_radii)):
        if palindrome_radii[i] > max_radius:
            max_radius, max_center = palindrome_radii[i], i

    # Convert back to indices in the original string.
    start, end = (max_center - max_radius) // 2, (max_center + max_radius - 1) // 2
    return s[start : end + 1]
