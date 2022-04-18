# ddd - Lab1 - Variant 4

## group name and group member

- Name:
  - ddd

- Member
  - Wang Qihang:
    - id: 212320003
    - email: Wqhlw@hdu.edu.cn
  - Wang Zehao:
    - id: 212320005
    - email: 15029930122@163.com

## Variant 4

### Set based on hash-map, separate chaining

You can use the built-in list for storing buckets and a bucket itself.

You need to check that your implementation correctly works with None value.

## contribution

Wang Qihang Completed the mutable.py

Wang Zehao Completed the test_mutable.py

## Changelog

- 16.04.2022 - 1
  - Add Wang Zehao upload test_mutable.py
- 15.04.2022 - 1
  - Wang Qihang upload mutable.py
- 14.04.2022 - 0
  - Initial

## Design notes

- Implementation restrictions:
  - The length of the hash table is fixed

- Advantages of unittest:
  - Support automated testing
  - Secondary development is convenient
  - Organize test cases together by class

- Disadvantages of unittest:
  - Must be written in TestCase subclass
  - Must write test method
  - Difficult to expand
 
- Advantages of PBT tests:
  - Check with automatically generated input data to ensure enough test cases
  - Allows developers to increase test coverage and effectively save time

- Disadvantages of PBT tests:
  - Not covering all examples
