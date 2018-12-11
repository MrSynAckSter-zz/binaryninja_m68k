import traceback
import sys
import os
import platform
import struct
try:
    from binaryninja import *
except ImportError:
    if platform.mac_ver()[0]:
        sys.path.append("/Applications/Binary Ninja.app/Contents/Resources/python")
        from binaryninja import *

InstructionNames = [
    #000...
	[],
    #0100
    [],
    #0101
    [],
    #0111,
    [],
    #1000,
    [],
    #1001,
    [],
    #1011,
    [],
    #1100
    [],
    #1101
    [],
    #No 1111
]

InstructionOperandTypes = [

]

OperandLengths = [

]

OperandTokens = [

]

OperandIL = [

]

SourceOperandsIL = [

]

DestOperandsIL = [

]

def cond_branch(il, cond, dest):
	#learn how branching works 

def jump(il, dest):

def call(il, src_op, src, src_value):


InstructionIL = {

}



class M68K(Architecture):
    name = 'M68K'
    address_size = 4
    default_int_size = 2

    regs = {
        'D0': RegisterInfo('D0', 4),
        'D1': RegisterInfo('D1', 4),
        'D2': RegisterInfo('D2', 4),
        'D3': RegisterInfo('D3', 4),
        'D4': RegisterInfo('D4', 4),
        'D5': RegisterInfo('D5', 4),
        'D6': RegisterInfo('D6', 4),
        'D7': RegisterInfo('D7', 4),
        'A0': RegisterInfo('A0', 4),
        'A1': RegisterInfo('A1', 4),
        'A2': RegisterInfo('A2', 4),
        'A3': RegisterInfo('A3', 4),
        'A4': RegisterInfo('A4', 4),
        'A5': RegisterInfo('A5', 4),
        'A6': RegisterInfo('A6', 4),
        'USP': RegisterInfo('USP', 4),
        'SSP': RegisterInfo('SSP', 4),
        'PC': RegisterInfo('PC', 4),
        'SR': RegisterInfo('SR',4)


    }

    flags = ['x','n','z','v','c'] # there's actually more. Maybe we simulate them? 

    flag_write_types = ["*"] # no good documentation of this. 

    flags_written_by_flag_write_type = {
        '*': ['v', 'n', 'c', 'z'] #they are independent 
     } 

    flag_roles = {
        'c': FlagRole.CarryFlagRole,
        'n': FlagRole.NegativeSignFlagRole,
        'z': FlagRole.ZeroFlagRole,
        'v': FlagRole.OverflowFlagRole
        'x': FlagRole.PositiveSignFlagRole #just guessing, this is really an extend flag. 
    }

    flags_required_for_flag_condition = {
        LowLevelILFlagCondition.LLFC_UGE: ['c'],       #Keeping the same as others have set it. Review later. 
        LowLevelILFlagCondition.LLFC_ULT: ['c'],
        LowLevelILFlagCondition.LLFC_SGE: ['n', 'v'],
        LowLevelILFlagCondition.LLFC_SLT: ['n', 'v'],
        LowLevelILFlagCondition.LLFC_E: ['z'],
        LowLevelILFlagCondition.LLFC_NE: ['z'],
        LowLevelILFlagCondition.LLFC_NEG: ['n'],
        LowLevelILFlagCondition.LLFC_POS: ['n']
    }

    stack_pointer = 'USP'

    def decode_instruction(self, data, addr):

    #learn more about instruction decoding before implementing

    def get_instruction_info(data,addr): 
    	#read more documentation


    def get_instruction_text(data,addr): 
    	#read more documentation 

    def get_instruction_low_level_il(data, addr, il):
    	#read more documentation

    	#additional overloads for branching behavior 
    def convert_to_nop(self, data, addr):
        return "\xea" * len(data)

    #always_branch(data, addr)
    #assemble(code, addr=0)
    #invert_branch(data, addr)
    #is_always_branch_patch_available(data, addr)
    #is_invert_branch_patch_available(data, addr)[
    #is_never_branch_patch_available(data, addr)
    #is_skip_and_return_value_patch_available(data, addr)
    #is_skip_and_return_zero_patch_available(data, addr)[
    #perform_is_never_branch_patch_available(data, addr)
    #skip_and_return_value(data, addr, value)
    

class DefaultCallingConvention(CallingConvention):
    int_arg_regs = ['D0', 'D1', 'D2', 'D3']
    int_return_reg = 'D7'
   


M68K.register()
arch = Architecture['M68K']
#not sure if we have consistent calling conventions for this. 
#arch.register_calling_convention(DefaultCallingConvention(arch, 'default'))
standalone = arch.standalone_platform
#standalone.default_calling_convention = arch.calling_conventions['default']




