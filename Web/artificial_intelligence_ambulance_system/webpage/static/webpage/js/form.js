<script type="text/javascript">
			var colleges=['�Ӿǰ|','�u�ǰ|','�س]�ǰ|','���ľǰ|','�ؿv�M�~�ǰ|','��ڬ�޻P�޲z�ǰ|','��q�ǰ|','�H����|�ǰ|','�z�ǰ|','�g��޲z�ǰ|','����]�p�ǰ|','���t�ǲ�'];
			var collegeSelect=document.getElementById("college-list");
			var inner="";
			for(var i=0;i<colleges.length;i++){
				inner=inner+'<option value=i>'+colleges[i]+'</option>';
			}
			collegeSelect.innerHTML=inner;


			var sectors=new Array();
			sectors[0]=['�|�p�Ǩt ',' ��ڸg��P�T���Ǩt' ,' ��ڸg��P�T���Ǩt��ڥ��~�޲z���^�y�Ǥh�Z' ,' �]�|�Ǩt' ,' �X�@�g�ٺ[���|�Ʒ~�g��Ǩt' ,' �έp�Ǩt ',' �g�پǨt' ,' ���~�޲z�Ǩt' ,' ��P�Ǩt' ,' ��ڥ��~�޲z�Ǥh�Ǧ�ǵ{(�^�y�M�Z)' ,' �ӾǶi�׾Ǥh�Ǧ�ǵ{' ,'�]�g�k�߬�s��' ,' ��޺޲z�Ӥh�Ǧ�ǵ{' ,' ���~�Ӥh�M�Z' ,' �ӾǱM�~�Ӥh�b¾�Ǧ�ǵ{' ,'�Ӿǳդh�Ǧ�ǵ{ '];
			sectors[1]=['����P�q�����U�u�{�Ǩt ',' �ֺ��P�ƦX���ƾǨt ',' �u�~�u�{�P�t�κ޲z�Ǩt ',' �ƾǤu�{�Ǩt ',' ��ӻP�t�Τu�{�Ǩt ',' ��K�t�γ]�p�Ǥh�Ǧ�ǵ{ ','�q�n�Ӥh�Ǧ�ǵ{ ',' ���෽��޺Ӥh�Ǧ�ǵ{ ',' �зN�]�p�Ӥh�Ǧ�ǵ{ ',' ���ƻP�s�y�u�{�Ӥh�b¾�M�Z ',' ����s�y�P�u�{�޲z�Ӥh�b¾�Ǧ�ǵ{ ','����P��Ťu�{�դh�Ǧ�ǵ{ '];
			sectors[2]=['�g��u�{�Ǩt ',' ���Q�u�{�P�귽�O�|�Ǩt ',' �����p�e�P�Ŷ���T�Ǩt ',' �B��P���y�Ǩt ',' �g�a�޲z�Ǩt ','���[�P�C�ͺӤh�Ǧ�ǵ{ ',' �M�׺޲z�Ӥh�b¾�Ǧ�ǵ{ ',' �س]�Ӥh�b¾�Ǧ�ǵ{ ','�g����Q�u�{�P�س]�W���դh�Ǧ�ǵ{ '];
			sectors[3]=['���I�޲z�P�O�I�Ǩt ',' �]�Ȫ��ľǨt ',' �]�Ȥu�{�P���Ǥh�Ǧ�ǵ{ ','���ĺӤh�b¾�Ǧ�ǵ{ ','���ĳդh�Ǧ�ǵ{ '];
			sectors[4]=['�ؿv�M�~�ǰ|�Ǥh�Z ',' �ؿv�Ǥh�Ǧ�ǵ{ ',' �Ǥ��]�p�Ǥh�Ǧ�ǵ{ ',' �Ǥ��]�p�i�׾Ǥh�Z ',' �зs�]�p�Ǥh�Ǧ�ǵ{ ',' �ؿv�Ӥh�Ǧ�ǵ{ ',' �ؿv�Ӥh�b¾�Ǧ�ǵ{','�D�w�������Ӯa�z�u�j�ǰӾǻP�зs���Ǥh�Ǧ�ǵ{ ','����t����{�ߤj�ǰӾǤj�ƾڤ��R���Ǥh�Ǧ�ǵ{ ']
			sectors[5]=['���괶��j�ǹq����T���Ǥh�Ǧ�ǵ{ ','��Z���ĩԤ��Ĥj�Ǫ��y������޲z�P�зs�з~���Ӥh�Ǧ�ǵ{ ','��ڸg��޲z�Ӥh�Ǧ�ǵ{ '];
			sectors[6]=['��T�u�{�Ǩt ',' �q���u�{�Ǩt ',' �q�l�u�{�Ǩt ',' �۰ʱ���u�{�Ǩt ',' �q�T�u�{�Ǩt',' ��q�����t�a�A�Z ','��T�q���u�{�Ӥh�b¾�Ǧ�ǵ{ ',' ���~��o�Ӥh�M�Z ',' �����T�[����u�{�Ӥh�Ǧ�ǵ{ ',' ������޺Ӥh�b¾�Ǧ�ǵ{ ','�q���P�q�T�u�{�դh�Ǧ�ǵ{ ',' ���z�p�����~�դh�Ǧ�ǵ{'];
			sectors[7]=['�����Ǩt ',' �~��y��Ǩt ','���v�P�媫��s�� ',' ���@�ưȻP���|�зs��s�� '];
			sectors[8]=['���μƾǨt ',' ���Ҥu�{�P��ǾǨt ',' ���Ƭ�ǻP�u�{�Ǩt ',' ���q�Ǩt ','�L�n���оǤ��� ',' ���z�оǬ�s���� '];
			sectors[9]=['�g��޲z�Ӥh�b¾�Ǧ�ǵ{ ',' �q�l�ӰȺӤh�b¾�M�Z '];
			sectors[10]=[];
			sectors[11]=['�q�ѱШ|���� ',' ���ݾǰ| ','�~�y�оǤ��� ',' ��y��оǤ��� ','���հ�ڥͤj�@�����t�Ǥh�Z '];
			function changeCollege(index){
				var Sinner="";
				for(var i=0;i<sectors[index].length;i++){
					Sinner=Sinner+'<option value=i>'+sectors[index][i]+'</option>';
				}
				var sectorSelect=document.getElementById("sector-list");
				sectorSelect.innerHTML=Sinner;
			}
			changeCollege(document.getElementById("college-list").selectedIndex);
		</script>