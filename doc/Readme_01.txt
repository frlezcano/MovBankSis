Vision - Application Flow Diagram
Editing: aabancos            ┌──────────────┐
                             │   aabancos   │
                             └──┬─────<Menu>┘
                                │
                                │
    ┌──────────────────┬────────┴─────────┬──────────────────┐
  Ver Depositos      Listar Depositos   List.Cred.Ajuste   List.Deb.Otros C
    │                  │                  │                  │
 ┌──┴───────────┐   ┌──┴───────────┐   ┌──┴───────────┐   ┌──┴───────────┐
 │ brdepositos  │   │ usdepositos  │   │ usdepajuste  │   │ usotroscarg  │
 └──┬───<Browse>┘   └────────<User>┘   └────────<User>┘   └────────<User>┘
    │
    │
    └──────────────────┬──────────────────┐
                     Agregar            Modificar
                       │                  │
                    ┌──┴───────────┐   ┌──┴───────────┐
                    │   apdeposi   │   │ updepositos  │
                    └──────<Append>┘   └──────<Update>┘




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



Vision - Visual Query Editor  
Frame: apdeposi
          ┌───────────<Append>┐  Display on Form     
          │stdmvcta           │ /   
          ├───────────────────┼─┬─Assignment/Default──────────┐
┌───────a─┤cod_banco          │y│                             │
│         │cod_ctacte         │y│                             │
│         │fec_ope            │y│                             │
│         │fec_recaud         │y│                             │
│         │doc_ref            │y│                             │
│         │cod_ope            │y│                             │
│         │tip_pag            │n│'O'                          │
│         │monto_gs           │y│                             │
│         │estado             │n│'N'                          │
│         │glosa              │y│                             │
│         │tip_mov_ba         │y│                             │
│         │cod_error          │n│                             │
│         │nro_mov            │n│                             │
│         └───────────────────┴─┴─────────────────────────────┘
│
│                                 Display on Form    
│         ┌───────────<Lookup>┐  /  Order in Popup   
│         │stbbanco           │ /  /        Qualify Lookup (y/n): n
│         ├───────────────────┼─┬───┬───Column Title─┐
└───────a─┤cod_banco          │n│1  │Cod Banco       │
          │nom_banco          │y│2  │Nombre Banco    │
          │conc_estado        │n│   │                │
          │conc_fec_concil    │n│   │                │
          │conc_arch_recibido │n│   │                │
          │conc_arch_cargado  │n│   │                │
          │conc_list_previos  │n│   │                │
          │conc_list_post     │n│   │                │
          │conc_fec_ant       │n│   │                │
          │x_monto            │n│   │                │
          │x_fecha_1          │n│   │                │
          │x_fecha_dia        │n│   │                │
          │x_fecha_mes        │n│   │                │
          │x_fecha_ano        │n│   │                │
          │x_beneficiario     │n│   │                │
          │x_guaranies_1      │n│   │                │
          │x_guaranies_2      │n│   │                │
          │x_guaranies_3      │n│   │                │
          │x_tfecha           │n│   │                │
          │x_truc             │n│   │                │
          │x_tconcepto        │n│   │                │
          │x_tvalor           │n│   │                │
          │x_tbanco           │n│   │                │
          │x_tcuenta          │n│   │                │
          │x_tcheque          │n│   │                │
          │y_monto            │n│   │                │
          │y_fecha_1          │n│   │                │
          │y_fecha_dia        │n│   │                │
          │y_fecha_mes        │n│   │                │
          │y_fecha_ano        │n│   │                │
          │y_beneficiario     │n│   │                │
          │y_guaranies_1      │n│   │                │
          │y_guaranies_2      │n│   │                │
          │y_guaranies_3      │n│   │                │
          │y_tfecha           │n│   │                │
          │y_truc             │n│   │                │
          │y_tconcepto        │n│   │                │
          │y_tvalor           │n│   │                │
          │y_tbanco           │n│   │                │
          │y_tcuenta          │n│   │                │
          │y_tcheque          │n│   │                │
          │l_guaranies_1      │n│   │                │
          │l_guaranies_2      │n│   │                │
          └───────────────────┴─┴───┴────────────────┘



┌──────────────────────────────────────────────────────────────────────────────┐
│"Append-End" Escape Code                                                      │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│   IF tip_mov_ba = 'CV' AND cod_ope = 8 THEN                                  │
│      UPDATE stmchequ                                                         │
│      SET est_che = 'I',                                                      │
│          fec_cobro= NULL,                                                    │
│          fec_entre = NULL                                                    │
│      WHERE cod_banco  = :g_cod_banco                                         │
│        AND cod_ctacte = :g_cod_ctacte                                        │
│        AND fec_ope    = :g_fec_ope                                           │
│        AND no_che_tes = :g_doc_ref                                           │
│        AND cod_ope    = :g_cod_ope                                           │
│        ;                                                                     │
│        INQUIRE_INGRES (IIerrorno = ERRORNO,                                  │
│                        IIrowcount= ROWCOUNT);                                │
│                                                                              │
│        IF IIerrorno <> 0 THEN                                                │
│           ROLLBACK;                                                          │
│           MESSAGE                                                            │
│   'Ha ocurrido un error al recuperar datos del Cheque Cobrado...'            │
│           WITH STYLE=POPUP;                                                  │
│           RESUME;                                                            │
│        ELSEIF IIrowcount =0 THEN                                             │
│           ROLLBACK;                                                          │
│           MESSAGE 'No existe el Cheque...'                                   │
│           WITH STYLE=POPUP;                                                  │
│           RESUME;                                                            │
│        ENDIF;                                                                │
│   ENDIF;                                                                     │
│                                                                              │
│   REPEATED                                                                   │
│   UPDATE STMCUENTA                                                           │
│   SET sal_depdia = IFNULL(sal_depdia,0) + :monto_gs                          │
│   WHERE cod_banco = :cod_banco                                               │
│   AND cod_ctacte= :cod_ctacte;                                               │
│                                                                              │
│   INQUIRE_INGRES (IIerrorno = ERRORNO,                                       │
│                   IIrowcount= ROWCOUNT);                                     │
│                                                                              │
│   IF IIerrorno <> 0 THEN                                                     │
│           ROLLBACK;                                                          │
│           MESSAGE 'Error al recuperar datos del Deposito...'                 │
│           WITH STYLE=POPUP;                                                  │
│           RESUME;                                                            │
│   ELSEIF IIrowcount =0 then                                                  │
│            ROLLBACK;                                                         │
│            MESSAGE 'No se pudo actualizar Dep.del Dia del Banco'+            │
│            ' Avise al tecnico' WITH STYLE=POPUP;                             │
│            RESUME;                                                           │
│   ENDIF;                                                                     │
│                                                                              │
│   IF tip_mov_ba='DJ'  THEN                                                   │
│                                                                              │
│               UPDATE STMCUENTA                                               │
│               SET sal_actbco= ifnull(sal_actbco,0) + :monto_gs               │
│               WHERE cod_banco = :cod_banco                                   │
│                 AND cod_ctacte= :cod_ctacte;                                 │
│                                                                              │
│                                                                              │
│             INQUIRE_INGRES (IIerrorno = ERRORNO,                             │
│                             IIrowcount= ROWCOUNT);                           │
│                                                                              │
│             IF IIerrorno <> 0 THEN                                           │
│                ROLLBACK;                                                     │
│                MESSAGE 'Error al recuperar datos del Deposito...'            │
│                WITH STYLE=POPUP;                                             │
│                RESUME;                                                       │
│             ELSEIF IIrowcount < 1 THEN                                       │
│                ROLLBACK;                                                     │
│                MESSAGE 'No se pudo actualizar el saldo del Banco, ' +        │
│                 'la operacion '                                              │
│                + 'ha sido cancelada.  Consulte con el Tecnico.'              │
│                WITH STYLE=POPUP;                                             │
│                RESUME;                                                       │
│             ENDIF;                                                           │
│   ENDIF;                                                                     │
└──────────────────────────────────────────────────────────────────────────────┘
  
Source Code


BEGIN
    VALIDATE;   /* VALIDATE all fields on form */

    MESSAGE 'Grabando . . .';
                                                    /*# BEGIN Insert\Master */
    REPEATED INSERT
    INTO stdmvcta(cod_banco, cod_ctacte, fec_ope, fec_recaud, doc_ref,
      cod_ope, tip_pag, monto_gs, estado, glosa, tip_mov_ba, cod_error,
      nro_mov)
    VALUES(cod_banco, cod_ctacte, fec_ope, fec_recaud, doc_ref, cod_ope,
    'O',
    monto_gs,
    'N',
    glosa, tip_mov_ba,
    NULL,
    NULL) ;
                                                      /*# END Insert\Master */

    INQUIRE_INGRES (IIerrorno = ERRORNO,
                    IIrowcount= ROWCOUNT); /*Agregado por Celsi*/
    IF (IIerrorno != 0) THEN
        ROLLBACK WORK;
        CALLPROC beep();        /* 4gl built-in procedure */
        MESSAGE 'An error occurred while saving changes.'
              + ' Details about the error were described'
              + ' by the message immediately preceding this one.'
              + ' The "Save" operation was not performed.'
              + ' Please correct the error and select "Save" again.'
              WITH STYLE = POPUP;
        RESUME;
    ENDIF;

    /* Agregado por Celsi */
    IF (IIrowcount = 0) THEN
        ROLLBACK WORK;
        CALLPROC beep();        /* 4gl built-in procedure */
        MESSAGE 'An error occurred while saving changes. INTEGRITY'
              + ' Details about the error were described'
              + ' by the message immediately preceding this one.'
              + ' The "Save" operation was not performed.'
              + ' Please correct the error and select "Save" again.' WITH STYLE
= POPUP;
        RESUME;
    ENDIF;
    /* Hasta aqui */

                                                       /*# BEGIN Append-End */
       IF tip_mov_ba = 'CV' AND cod_ope = 8 THEN
          UPDATE stmchequ
          SET est_che = 'I',
              fec_cobro= NULL,
              fec_entre = NULL
          WHERE cod_banco  = :g_cod_banco
            AND cod_ctacte = :g_cod_ctacte
            AND fec_ope    = :g_fec_ope
            AND no_che_tes = :g_doc_ref
            AND cod_ope    = :g_cod_ope
            ;
            INQUIRE_INGRES (IIerrorno = ERRORNO,
                            IIrowcount= ROWCOUNT);

            IF IIerrorno <> 0 THEN
               ROLLBACK;
               MESSAGE
       'Ha ocurrido un error al recuperar datos del Cheque Cobrado...'
               WITH STYLE=POPUP;
               RESUME;
            ELSEIF IIrowcount =0 THEN
               ROLLBACK;
               MESSAGE 'No existe el Cheque...'
               WITH STYLE=POPUP;
               RESUME;
            ENDIF;
       ENDIF;

       REPEATED
       UPDATE STMCUENTA
       SET sal_depdia = IFNULL(sal_depdia,0) + :monto_gs
       WHERE cod_banco = :cod_banco
       AND cod_ctacte= :cod_ctacte;

       INQUIRE_INGRES (IIerrorno = ERRORNO,
                       IIrowcount= ROWCOUNT);

       IF IIerrorno <> 0 THEN
               ROLLBACK;
               MESSAGE 'Error al recuperar datos del Deposito...'
               WITH STYLE=POPUP;
               RESUME;
       ELSEIF IIrowcount =0 then
                ROLLBACK;

                MESSAGE 'No se pudo actualizar Dep.del Dia del Banco'+
                ' Avise al tecnico' WITH STYLE=POPUP;
                RESUME;
       ENDIF;

       IF tip_mov_ba='DJ'  THEN

                   UPDATE STMCUENTA
                   SET sal_actbco= ifnull(sal_actbco,0) + :monto_gs
                   WHERE cod_banco = :cod_banco
                     AND cod_ctacte= :cod_ctacte;


                 INQUIRE_INGRES (IIerrorno = ERRORNO,
                                 IIrowcount= ROWCOUNT);

                 IF IIerrorno <> 0 THEN
                    ROLLBACK;
                    MESSAGE 'Error al recuperar datos del Deposito...'
                    WITH STYLE=POPUP;
                    RESUME;
                 ELSEIF IIrowcount < 1 THEN
                    ROLLBACK;
                    MESSAGE 'No se pudo actualizar el saldo del Banco, ' +
                     'la operacion '
                    + 'ha sido cancelada.  Consulte con el Tecnico.'
                    WITH STYLE=POPUP;
                    RESUME;
                 ENDIF;
       ENDIF;
                                                        ;/*# END Append-End */

    COMMIT WORK;

    INQUIRE_INGRES (IIerrorno = ERRORNO,
                    IIrowcount= ROWCOUNT);
    IF (IIerrorno != 0) THEN
        ROLLBACK WORK;
        MESSAGE 'An error occurred while Saving this data.'
              + ' Details about the error were described by'
              + ' the message immediately preceding this one.'
              + ' The "Save" operation was not performed.'
              + ' Please correct the error and select "Save"'
              + ' again.'
              WITH STYLE = POPUP;
        RESUME;
    ENDIF;

    /* Agregado por Celsi */
    IF (IIrowcount = 0) THEN
        ROLLBACK WORK;
        MESSAGE 'An error occurred while Saving this data. INTEGRITY.'
              + ' Details about the error were described by'
              + ' the message immediately preceding this one.'
              + ' The "Save" operation was not performed.'
              + ' Please correct the error and select "Save"'
              + ' again.'
              WITH STYLE = POPUP;
        RESUME;
    ENDIF;
    /* Hasta aqui */

    SET_FORMS FORM (CHANGE = 0);
    IF (IIclear = 'y') THEN
        MODE 'fill';        /* display default values + clear simple fields */
        SET_FORMS FORM (MODE = 'update');   /* keep cursor off Query-only flds*/
    ENDIF;

END


'ListOpciones' (VALIDATE = 0, ACTIVATE = 0,
        EXPLANATION = 'Show valid values for current field'),
                II_QUERY = SELECT DISTINCT cod_banco, nom_banco
                           FROM stbbanco
                           ORDER BY cod_banco, nom_banco;
                II_FIELD1 = 'cod_banco';
                II_FIELD2 = 'nom_banco';


AFTER FIELD 'tip_mov_ba' =
BEGIN
                                      /*# BEGIN After-Field-Exit\tip_mov_ba */
                SET_FORMS FIELD apdeposi
                          (displayonly (fec_recaud) = on);

                IF tip_mov_ba = 'DR' THEN
                   des_tip_mov_ba = 'DEPOSITO RECAUDACION';
                   SET_FORMS FIELD apdeposi
                             (displayonly (fec_recaud) = off);
                ELSE
                   fec_recaud = ' ';
                   IF tip_mov_ba = 'DT' THEN
                      des_tip_mov_ba = 'DEPOSITO TRANSFERENCIA';
                   ELSEIF tip_mov_ba = 'DV' THEN
                      des_tip_mov_ba = 'DEPOSITO POR REVERSION SIT-01';
                   ELSEIF tip_mov_ba = 'DF' THEN
                      des_tip_mov_ba = 'DEPOSITO POR CIERRE SIT-02 FONDO FIJO';
                   ELSEIF tip_mov_ba = 'DA' THEN
                      des_tip_mov_ba =
        'DEPOSITO POR CIERRE SIT-02 AGENTE RESPONSABLE';
                   ELSEIF tip_mov_ba = 'DP' THEN
                      des_tip_mov_ba =
        'DEPOSITO POR CIERRE SIT-02 DESEMBOLSOS PARCIALES';
                   ELSEIF tip_mov_ba = 'DO' THEN
                      des_tip_mov_ba = 'DEPOSITOS DE OTROS (TERCEROS)';
                   ELSEIF tip_mov_ba = 'DJ' THEN
                      des_tip_mov_ba = 'DEPOSITOS DE AJUSTES';
                   ELSEIF tip_mov_ba = 'CV' THEN
                      des_tip_mov_ba = 'CREDITOS VARIOS';
                  ELSE
                     MESSAGE 'Tipo de Movimiento Bancario invalido. '
                             + 'Solo pueden ser DR, DT, DV, DF, DA, DP, DO, '+
                               'DJ y CV.'
                     WITH STYLE = POPUP;
                     tip_mov_ba = 'DR';
                     des_tip_mov_ba = 'DEPOSITO RECAUDACION';
                     RESUME FIELD tip_mov_ba;
                 ENDIF;
             ENDIF;
                                       ;/*# END After-Field-Exit\tip_mov_ba */
    RESUME NEXT;
END

AFTER FIELD 'monto_gs' =
BEGIN
                                        /*# BEGIN After-Field-Exit\monto_gs */
    IF NOT monto_gs > 0 THEN
       MESSAGE 'Ingrese el Importe del Documento'
          WITH STYLE = POPUP;
       RESUME FIELD monto_gs;
    ENDIF;
                                         ;/*# END After-Field-Exit\monto_gs */
    RESUME NEXT;
END

AFTER FIELD 'fec_recaud' =
BEGIN
                                      /*# BEGIN After-Field-Exit\fec_recaud */
    IF fec_recaud = ' ' THEN
       MESSAGE 'Ingrese Fecha de la Recaudacion.'
          WITH STYLE = POPUP;
       RESUME FIELD fec_recaud;
    ENDIF;
                                       ;/*# END After-Field-Exit\fec_recaud */
    RESUME NEXT;
END

AFTER FIELD 'fec_ope' =
BEGIN
                                         /*# BEGIN After-Field-Exit\fec_ope */
    IF fec_ope = ' ' THEN
       MESSAGE 'Ingrese Fecha del Documento'
          WITH STYLE = POPUP;
       RESUME FIELD fec_ope;
    ENDIF;
                                          ;/*# END After-Field-Exit\fec_ope */
    RESUME NEXT;
END

AFTER FIELD 'doc_ref' =
BEGIN
                                         /*# BEGIN After-Field-Exit\doc_ref */
    If Not doc_ref > 0 THEN
       MESSAGE 'Ingrese el numero de documento de referencia'
          WITH STYLE = POPUP;
       RESUME FIELD doc_ref;
    EndIf;
                                          ;/*# END After-Field-Exit\doc_ref */
    RESUME NEXT;
END

AFTER FIELD 'cod_ope' =
BEGIN
                                         /*# BEGIN After-Field-Exit\cod_ope */
                   IF tip_mov_ba = 'DR' THEN
                      IF cod_ope != 1 AND cod_ope != 2 AND cod_ope != 3
                         AND cod_ope != 21 THEN
                         MESSAGE 'Debe Ingresar "1", "2", "3" o "21"'
                         WITH STYLE=POPUP;
                         RESUME FIELD cod_ope;
                      ENDIF;
                   ELSEIF tip_mov_ba = 'CV' THEN
                      IF cod_ope != 8 THEN
                         MESSAGE 'Debe Ingresar "8" ' WITH STYLE=POPUP;
                         RESUME FIELD cod_ope;
                      ELSE
                         CALLFRAME uscheqcob ();

                         cod_banco = g_cod_banco;
                         cod_ctacte = g_cod_ctacte;
                         monto_gs = IFNULL(g_monto_gs, 0);

                         SET_FORMS FIELD apdeposi
                                (displayonly (cod_banco) = on);

                            SELECT :nom_banco = nom_banco
                              FROM stbbanco b
                             WHERE b.cod_banco = :cod_banco
                            ;
                            INQUIRE_INGRES(g_rows = ROWCOUNT,
                                           g_error = ERRORNO);
                            COMMIT;
                          IF g_error <> 0 THEN
                              MESSAGE
         'Ha ocurrido un error al seleccionar el Banco...'
                              WITH STYLE=POPUP;
                              RESUME FIELD cod_banco;
                          ELSEIF g_rows < 1 THEN
                              MESSAGE 'Codigo Banco Inexistente...'
                              WITH STYLE=POPUP;
                              RESUME FIELD cod_banco;
                          ENDIF;
                          /*SET_FORMS FIELD apdeposi
                                    (displayonly (cod_banco) = off);*/

                         SET_FORMS FIELD apdeposi
                                (displayonly (cod_ctacte) = on);

                            SELECT :nom_ctacte = nom_ctacte
                              FROM stmcuenta c
                             WHERE c.cod_banco = :cod_banco
                               AND c.cod_ctacte = :cod_ctacte
                            ;
                            INQUIRE_INGRES(g_rows = ROWCOUNT,
                                           g_error = ERRORNO);
                            COMMIT;
                          IF g_error <> 0 THEN
                              MESSAGE
          'Ha ocurrido un error al seleccionar la Cuenta...'
                              WITH STYLE=POPUP;
                              RESUME FIELD cod_ctacte;
                          ELSEIF g_rows < 1 THEN
                              MESSAGE 'Codigo Cuenta Inexistente...'
                              WITH STYLE=POPUP;
                              RESUME FIELD cod_ctacte;
                          ENDIF;
                          /*SET_FORMS FIELD apdeposi
                                    (displayonly (cod_ctacte) = off);*/

                         SET_FORMS FIELD apdeposi
                                (displayonly (monto_gs) = on);
                      ENDIF;
                   ELSE
                      IF cod_ope < 1 OR cod_ope > 49 THEN
                         MESSAGE 'El codigo de Operacion debe ser del 1 al 49'
                         WITH STYLE=POPUP;
                         RESUME FIELD cod_ope;
                      ENDIF;
                   ENDIF;
                   SELECT :des_ope = des_ope
                     FROM stbopeba
                    WHERE cod_ope = :cod_ope;
                    INQUIRE_INGRES(g_rows = ROWCOUNT,
                                   g_error = ERRORNO);
                    COMMIT;
                    IF g_error <> 0 THEN
                       ROLLBACK;
                       MESSAGE 'Error al seleccionar el Cod. de Operacion'
                       WITH STYLE=POPUP;
                       RESUME ;
                    ELSEIF g_rows < 1 THEN
                      MESSAGE 'Codigo de Operacion Inexistente'
                      WITH STYLE=POPUP;
                      RESUME FIELD cod_ope;
                    ENDIF;
                    IF tip_mov_ba = 'DR' THEN
                        glosa = 'Recaudacion de Fecha '+varchar(fec_recaud);
                    ENDIF;
                                          ;/*# END After-Field-Exit\cod_ope */
    RESUME NEXT;
END

AFTER FIELD 'cod_ctacte' =
BEGIN
                                      /*# BEGIN After-Field-Exit\cod_ctacte */
       IF NOT cod_ctacte > 0 THEN
           MESSAGE 'Debe Ingresar Codigo Cta Cte o de Ahorro'
           WITH STYLE=POPUP;
           RESUME FIELD cod_ctacte;
       ELSE
           SELECT :nom_ctacte= nom_ctacte, :tip_cta = clase_cta
             FROM stmcuenta
           WHERE cod_banco = :cod_banco
             AND cod_ctacte= :cod_ctacte;

           INQUIRE_INGRES(g_error = ERRORNO,
                          g_rows = ROWCOUNT);
           COMMIT;
          IF g_error <> 0 THEN
             ROLLBACK ;
             MESSAGE 'Error al seleccionar la Cuenta Cte...'
              WITH STYLE = POPUP;
             RESUME;
          ELSEIF g_rows < 1 THEN
             ROLLBACK ;
             MESSAGE 'Codigo Cta.Cte. Inexistente' WITH STYLE=POPUP;
             RESUME FIELD cod_ctacte;
           ELSE
              IF tip_cta = 'S' THEN
                 MESSAGE 'Cuenta no es de Caja de Ahorro' WITH STYLE=POPUP;
                 RESUME FIELD cod_ctacte;
              ENDIF;
           ENDIF;
       ENDIF;
                                       ;/*# END After-Field-Exit\cod_ctacte */
    RESUME NEXT;
END

AFTER FIELD 'cod_banco' =
BEGIN
    INQUIRE_FORMS FIELD '' (IIint = CHANGE);
    INQUIRE_FORMS FORM (IIobjname = MODE);
    IF (IIint = 1) AND (UPPERCASE(IIobjname) != 'QUERY') THEN
        apdeposi := REPEATED SELECT
        cod_banco = stbbanco.cod_banco, nom_banco = stbbanco.nom_banco
        FROM stbbanco
        WHERE stbbanco.cod_banco = :cod_banco;
        INQUIRE_INGRES (IIrowcount = ROWCOUNT);
        COMMIT WORK;            /* release shared locks */
        IF IIrowcount <= 0 THEN
            CALLPROC beep();    /* 4gl built-in function */
            MESSAGE IIinvalmsg1 + '"' +
              IFNULL(VARCHAR(:cod_banco), '') + '"' + IIinvalmsg2
              WITH STYLE = POPUP;
            RESUME;
        ENDIF;
    ENDIF;
                                       /*# BEGIN After-Field-Exit\cod_banco */
       IF NOT cod_banco > 0 THEN
          MESSAGE 'Ingrese el Codigo del Banco'
             WITH STYLE = POPUP;
          RESUME FIELD cod_banco;
       ENDIF;
       SELECT :nom_banco = nom_banco
        FROM stbbanco
       WHERE cod_banco = :cod_banco;

           INQUIRE_INGRES(g_error = ERRORNO,
                          g_rows = ROWCOUNT);
           IF g_error <> 0 THEN
              ROLLBACK ;
              MESSAGE 'Error al tratar de seleccionar el Banco...'
               WITH STYLE = POPUP;
              RESUME;
           ELSEIF g_rows < 1 THEN
              ROLLBACK ;
              MESSAGE 'Codigo Banco Inexistente'
              WITH STYLE=POPUP;
              RESUME FIELD cod_banco;
           ENDIF;
       COMMIT;
                                        ;/*# END After-Field-Exit\cod_banco */
    RESUME NEXT;
END


