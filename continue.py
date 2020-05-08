#compile continued

def comp_seq(exp,target,linkage): 
    if len(exp) == 1:
        seq = compiler.compile(exp[0],target,linkage)
        return seq
    else:
        cars= exp[0]
        crds= exp[1:]
        cardcode = compiler.compile(cars,target,'next')
        crdcode = comp_seq(crds,target,linkage)
        return preserve(['env','continue'],cardcode,crdcode)


        
def compile_lambda(exp,target,linkage):
    proc_entry = make_label('entry')
    after_lambda = make_label('after_lambda')
    lambda_linkage =''
    if linkage =='next':
        lambda_linkage = 'after_lambda'
    else:
        lambda_linkage = linkage

    inst = make_inst_sequence(['env']
                            ,[target]
                            ,['(assign {0} (op make_compiled_proc)  {1} (reg env))'.format(target,proc_entry)])
    proc_obj = end_with_link(lambda_linkage,inst)
    body = compile_labmda_body(exp,proc_entry)
    code_seq = tack_on_inst_seq(proc_obj,body)
    return append_seq(code_seq,after_lambda)


def compile_labmda_body(exp,proc_entry):
    formals = exp[1]
    inst = make_inst_sequence(['env','proc','argl']
                            ,['env']
                            ,[ proc_entry
                              ,'assign env (op compile_proc_env) (reg proc))'
                              ,'assign env (op extend_env) (const {0}) (reg argl) (reg env)'.format(formals)])

    body_seq = compiler.compile(exp[2],'val','return')

    allcode = append_seq(inst,body_seq)
    return allcode

def compile_application(exp,target,linkage):
    op = exp[1]
    oprands = exp[2]
    opcode = compiler.compile(op,'proc','next')
    oprandcode = [] 
    for oprd in oprands:
        opc = compiler.compile(oprd,'val','next')
        oprandcode.append(opc)

    argseq = construct_arg(oprandcode)
    comp_proc_call = compile_proc_call(target,linkage)
    
    pcode = preserve(['proc','continue']
                        ,argseq
                        ,comp_proc_call)

    allcode = preserve(['env','continue']
                       ,opcode
                       ,pcode)
    return allcode


    
    
    
