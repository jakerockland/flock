$ ->
    $("#lets-fly").on "click", ->
        onError = (jqXHR, textStatus, errorThrown) ->
            if jqXHR.status == 403
                location.href = "/login/twitter"
            else
                console.log jqXHR
                console.log textStatus
                console.log errorThrown
                alert "Your authentication with Twitter failed... Whoops."

        request = $.ajax({
            url: '/twitter',
            type: 'get'
        })

        request.done (data, textStatus, jqXHR) ->
            names = data.names
            tags = data.tags
            profs = data.profs
        request.fail onError

        return request
