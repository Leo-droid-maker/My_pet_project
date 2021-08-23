window.onload = function () {
    // $('.menu').on('click', 'a', function () {
    //     let target_href = event.target.href;
    //     if (target_href) {
    //         console.log('нужно перейти: ', target_href);
    //     }
    //     event.preventDefault();
    // });


    $('.basket_list').on('click', 'input[type="number"]', function () {
        // let target_href = $(this)
        let target_href = event.target;

        if (target_href) {
            $.ajax( {
                url: "/cart/edit/" + target_href.name + "/" + target_href.value + "/",

                success: function (data) {
                    $('.basket_list').html(data.result);
                    console.log('ajax done');
                },
            });
        }
        event.preventDefault();
    });
};