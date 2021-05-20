
                               ┌──────────────┐
-------------------------------│  Formulario  │---------------------------------
                               └──────────────┘

MCA-SIBA                       SISTEMA DE BANCOS                        apdeposi
                           ** Carga de Depositos **
────────────────────────────────────────────────────────────────────────────────

   Tipo Mov. Bancarios : c_ c_________________________________________________

   Operacion     : n_ c_____________________________

   Fecha Recaudacion:    c_________

   Fecha Deposito en Banco: c_________      Doc Ref: n_________

   Cod. Banco    : n_ c_____________________________

   Cta.Cte / Ahorro: n____________ c__________________________________

   Importe.......: z,___,___,___,___,___

   Observacion   : c_________________________________________________
----------------------------------End-of-Form-----------------------------------




                            ┌────────────────────────┐
----------------------------│  Campos de Formulario  │--------------------------
                            └────────────────────────┘

Tipo Mov. Bancarios :    tip_mov_ba
Operacion     :          cod_ope
Fecha Recaudacion:       fec_ope
Fecha Deposito en Banco: fec_recaud
Doc Ref:                 doc_ref
Cod. Banco    :          cod_banco
Cta.Cte / Ahorro:        cod_ctacte
Importe.......:          monto_gs
Observacion   :          glosa



                            ┌────────────────────────┐
----------------------------│           SQL          │--------------------------
                            └────────────────────────┘
stdmvcta
	INSERT
		CAMPOS(cod_banco, cod_ctacte, fec_ope, fec_recaud, doc_ref,cod_ope, tip_pag, monto_gs, estado, glosa, tip_mov_ba, cod_error,nro_mov)
		VALUES(cod_banco, cod_ctacte, fec_ope, fec_recaud, doc_ref,cod_ope,     'O', monto_gs,    'N', glosa, tip_mov_ba,      NULL,   NULL)


CV = 'CREDITOS VARIOS'
----------------------
IF tip_mov_ba = 'CV' AND cod_ope = 8 THEN
stmchequ
		UPDATE
			CAMPOS(est_che, fec_cobro, fec_entre)
			VALUES(  'I'  ,   NULL   ,    NULL  )
			WHERE (cod_banco  = cod_banco
            	   AND cod_ctacte = cod_ctacte
			   AND fec_ope    = fec_ope
			   AND no_che_tes = doc_ref
			   AND cod_ope    = cod_ope)

	stmcuenta
		UPDATE
			CAMPOS(sal_depdia)
			VALUES(IFNULL(sal_depdia,0) + monto_gs
			WHERE (cod_banco = cod_banco
			   AND cod_ctacte= cod_ctacte)


DJ = 'DEPOSITOS DE AJUSTES'
---------------------------
IF tip_mov_ba='DJ'  THEN
	stmcuenta
		UPDATE
			CAMPOS(sal_actbco)
			VALUES(ifnull(sal_actbco,0) + monto_gs)
			WHERE (cod_banco = :cod_banco
			   AND cod_ctacte= :cod_ctacte)
