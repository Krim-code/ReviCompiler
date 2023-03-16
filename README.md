# ReviCompiler
!(It`s the best img, realy)[]
## What is it?
  Compiler for the Revi language implemented using the LLVM and ANTLR4 libraries.
  #### The compiler supports the following data types:

1.  Int32
2.  Double
3.  Ability to output strings using the print() command

#### The following functionality is supported by the compiler:

1.  Functions and function calls
2.  While statement
3.  If statement
4.  Assignment operation
5.  Mathematical operations.
6.  TypeCast operations.

#### Example Revi Code:
    int test(int n){
        if(n < 2) {
          return 1;
        }
          return test(n-1) + test(n-2);
        }
        
    int main() {
        int x = test(40);
        print(x);
        return 0;
    }
#### Example non-optimized LLVM code:
    ModuleID = '<string>'
    source_filename = "<string>"
    target triple = "unknown-unknown-unknown"

    @fstr987 = internal constant [5 x i8] c"%i \0A\00"

    define i32 @test(i32 %.1) {
    entry:
      %.3 = icmp slt i32 %.1, 2
      br i1 %.3, label %entry.if, label %entry.endif

    entry.if:                                         ; preds = %entry
      ret i32 1

    entry.endif:                                      ; preds = %entry
      %.6 = sub i32 %.1, 1
      %.7 = call i32 @test(i32 %.6)
      %.8 = sub i32 %.1, 2
      %.9 = call i32 @test(i32 %.8)
      %.10 = add i32 %.7, %.9
      ret i32 %.10
    }

    define i32 @main() {
    entry:
      %.2 = call i32 @test(i32 40)
      %x = alloca i32, align 4
      store i32 %.2, i32* %x, align 4
      %.4 = bitcast [5 x i8]* @fstr987 to i8*
      %.5 = load i32, i32* %x, align 4
      %.6 = call i32 (i8*, ...) @printf(i8* %.4, i32 %.5)
      ret i32 0
    }

     declare i32 @printf(i8*, ...)
     
#### Example optimized LLVM code:
    ; ModuleID = '<string>'
    source_filename = "<string>"
    target triple = "unknown-unknown-unknown"

    @fstr987 = internal constant [5 x i8] c"%i \0A\00"

    ; Function Attrs: nounwind readnone
    define i32 @test(i32 %.1) local_unnamed_addr #0 {
    entry:
      %.31 = icmp slt i32 %.1, 2
      br i1 %.31, label %entry.if, label %entry.endif

    entry.if.loopexit:                                ; preds = %entry.endif
      %phi.bo = add i32 %.10, 1
      br label %entry.if

    entry.if:                                         ; preds = %entry.if.loopexit, %entry
      %accumulator.tr.lcssa = phi i32 [ 1, %entry ], [ %phi.bo, %entry.if.loopexit ]
      ret i32 %accumulator.tr.lcssa

    entry.endif:                                      ; preds = %entry, %entry.endif
      %.1.tr3 = phi i32 [ %.8, %entry.endif ], [ %.1, %entry ]
      %accumulator.tr2 = phi i32 [ %.10, %entry.endif ], [ 0, %entry ]
      %.6 = add nsw i32 %.1.tr3, -1
      %.7 = tail call i32 @test(i32 %.6)
      %.8 = add nsw i32 %.1.tr3, -2
      %.10 = add i32 %.7, %accumulator.tr2
      %.3 = icmp slt i32 %.1.tr3, 4
      br i1 %.3, label %entry.if.loopexit, label %entry.endif
    }

    ; Function Attrs: nofree nounwind
    define i32 @main() local_unnamed_addr #1 {
     entry:
      %.2 = tail call i32 @test(i32 40)
      %.6 = tail call i32 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([5 x i8], [5 x i8]* @fstr987, i64 0, i64 0), i32 %.2)
      ret i32 0
    }

    ; Function Attrs: nofree nounwind
    declare i32 @printf(i8* nocapture readonly, ...) local_unnamed_addr #1

    attributes #0 = { nounwind readnone }
    attributes #1 = { nofree nounwind }

#### Example TypeCast
    int main() {
        double x = <<double>>(33949);
        print(x);

        int y = <<int>>(34.556);
        print(y);
        return 1;
    }
