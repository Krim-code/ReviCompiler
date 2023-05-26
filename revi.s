	.text
	.def	 @feat.00;
	.scl	3;
	.type	0;
	.endef
	.globl	@feat.00
.set @feat.00, 0
	.file	"<string>"
	.def	 test;
	.scl	2;
	.type	32;
	.endef
	.globl	test
	.p2align	4, 0x90
test:
.seh_proc test
	pushq	%rsi
	.seh_pushreg %rsi
	pushq	%rdi
	.seh_pushreg %rdi
	subq	$40, %rsp
	.seh_stackalloc 40
	.seh_endprologue
	cmpl	$1, %ecx
	jg	.LBB0_3
	movl	$1, %eax
	jmp	.LBB0_2
.LBB0_3:
	movl	%ecx, %esi
	leal	-1(%rsi), %ecx
	callq	test
	movl	%eax, %edi
	addl	$-2, %esi
	movl	%esi, %ecx
	callq	test
	addl	%edi, %eax
.LBB0_2:
	addq	$40, %rsp
	popq	%rdi
	popq	%rsi
	retq
	.seh_handlerdata
	.text
	.seh_endproc

	.def	 main;
	.scl	2;
	.type	32;
	.endef
	.globl	main
	.p2align	4, 0x90
main:
.seh_proc main
	subq	$40, %rsp
	.seh_stackalloc 40
	.seh_endprologue
	movl	$40, %ecx
	callq	test
	movl	%eax, 36(%rsp)
	leaq	fstr43596(%rip), %rcx
	movl	%eax, %edx
	callq	printf
	xorl	%eax, %eax
	addq	$40, %rsp
	retq
	.seh_handlerdata
	.text
	.seh_endproc

	.section	.rdata,"dr"
fstr43596:
	.asciz	"%i \n"

