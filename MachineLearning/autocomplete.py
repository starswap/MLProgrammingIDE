def suggestAutocomplete(prefix):
        if len(prefix) > 0:
                if prefix[0] == "f":
                        results = ["apple","orange","pear","grape"]
                elif prefix[0] == "c":
                        results = ["Ford","Kia"]
                else:
                        results = []
        else:
                results = []
        return results
