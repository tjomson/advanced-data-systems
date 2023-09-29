# Questions

## 1
`What is the difference between the class Vector and the struct
UnifiedVectorFormat?`

Both are used to abstract vectors of different type. UnifiedVectorFormat repressents the data (only has GetData method), Vector repressents data with operations. Vector can convert to UnifiedVectorFormat. Buffer that is associated with the Vector.
Writing specialized code for every combination of vector types for every function is unfeasible due to the combinatorial explosion of possibilities. Instead of doing this, whenever you want to generically use a vector regardless of the type, the UnifiedVectorFormat can be used.
Each specific vector has specialized functions, but memory is associated with the Vector class.

## 2

`Why does ConstantVector not inherit from Vector?`

Vector has a lot of operations that ConstantVector does not need

## 3

`Where is a ConstantVector stored?`

With a pointer to a VectorBuffer. The buffer size is dependent of the type. e.g. a constant vector of int_64 will have size 8 bytes. CreateConstantVector calls make_buffer, which calls make_shared, which creates a shared_ptr.
DictionaryBuffer inherits from VectorBuffer, so here there is inheritance.
Allocations done by CollumnDataAllocator. If in memory, allocate on heap, if on disk, allocate somewhere that is in the buffermanager.
