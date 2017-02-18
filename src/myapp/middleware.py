from joins.models import Join

class ReferMiddleware():
    def process_request(self, request):
        
        
        ref_id = request.GET.get("ref")
        try:
            obj = Join.objects.get(ref_id = ref_id)
        except:
            obj = None
        if not obj == None:
            request.session['join_id_ref'] = obj.id
        
        
            
        
        